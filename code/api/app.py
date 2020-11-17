import scrapy
import subprocess
from flask_cors import CORS
from flask import Flask, jsonify, request
from collections import OrderedDict
from readability import Readability
from scrapy.crawler import CrawlerProcess
from webscraping.ws_priberam import Priberam
from summarization.similarity import Similarity
from summarization.spiders.default_spider import DefaultSpider

app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False
app.config['JSON_SORT_KEYS'] = False
app.config['PREV_SEARCH'] = ''


@app.route('/')
def index():
    return "Hello World!"

@app.route('/search')
def search():

    #1. Get the word
    expression = request.args.get('query')

    if(expression != ""):

        #2. Get the definitions of the word
        definitions = Priberam.scrap(expression)

        if definitions[0][0] == "Não foram encontrados resultados." or definitions[0][0] == "Funcionalidade ainda não implementada.":
            return jsonify(definitions[0][0])

        #3. Get the glosa of each definition
        #axios.get(/convert?phrase=)

        #4. Check the number of words from the definition that are in the DB
        searchResult = sortDefinitionsByReadability(definitions)

        #5. Present the definition with the highest number of matches
        response_object = buildResponse(expression, searchResult)

    else:
        response_object = None
    return jsonify(response_object)


#  Sort the sentences of the array of arrays by their calculated readability score
def sortDefinitionsByReadability(definitions):
    score = []
    for context in definitions:
        contextScore = {}
        for sentence in context:
            contextScore[sentence] = Readability.sentenceReadability(sentence)
        sorted_vec = sortDefinitions(contextScore)
        score.append(sorted_vec)
    return score


# Sort a dictionary in ascending order of values
def sortDefinitions(dictionary):
    return OrderedDict(sorted(dictionary.items(), key=lambda x: x[1]))


# Create response object
def buildResponse(expression, definition):
    priberam = "https://dicionario.priberam.org/" + expression
    infopedia = "https://www.infopedia.pt/dicionarios/lingua-portuguesa/" + expression
    lexico = "https://www.lexico.pt/" + expression
    wikipedia = "https://pt.wikipedia.org/wiki/" + expression
    info = [ infopedia, lexico, wikipedia]
    response = {'additionalInfo' : info,
            'definition' : definition,
            'expression' : expression.capitalize(),
            'source' : priberam
            }
    return response


@app.route('/summarization')
def summarization():

    expression = request.args.get('query')
    prevSentence = request.args.get('prev')
    startingPage = "https://pt.wikipedia.org/wiki/"

    if(expression != ""):

        #  Prevent crawl for the same word twice in a row.
        if expression != app.config['PREV_SEARCH']:

            subprocess.call(['rm', '-r', 'files', 'raw-files', 'summaries'])
            print("Remove Previous Search done")

            subprocess.call(['scrapy', 'runspider', 'summarization/spiders/default_spider.py', "--nolog", "-a", f"link={startingPage}", "-a", f"target={expression}"])
            print("Crawler done")

            subprocess.call(['python', 'summarization/htmlToTxt.py'])
            print("HTML to TXT done")

            subprocess.call(['python', "summarization/summarization.py"])
            print("Summarization done")

        if(prevSentence != ""):
            #  Calculate cosine similarity
            similarDefinitions = Similarity.similarity(prevSentence)

            #  Calculate the score and sort the similar Definitions
            resultsDefinitions = sortSimilarDefinitionsByReadability(similarDefinitions)

            response_object = resultsDefinitions
    else:
        response_object = None
    return jsonify(response_object)

#  Sort the sentences of the array by their calculated readability score
def sortSimilarDefinitionsByReadability(array):
    score = {}
    for sentence in array:
        score[sentence] = Readability.sentenceReadability(sentence)
    sortedScores = sortDefinitions(score)
    return sortedScores


if __name__ == "__main__":
    app.run(debug=True)
