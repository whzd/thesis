from flask import Flask, jsonify, request
from flask_cors import CORS
from webscraping.ws_priberam import Priberam
from db.querydb import DBQuery
from formula.lgp import LGPFormula

app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False

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

        #3. Get the glosa of each definition
        #axios.get(/convert?phrase=)

        #4. Check the number of words from the definition that are in the DB
        #sortedMatchList = buildSortedMatchList(definitions)
        print(matchResults(definitions))

        #5. Present the definition with the highest number of matches
        response_object = buildResponse(expression, definitions)

    else:
        response_object = None
    return jsonify(response_object)

# Create a dictionary of results orders by LGP readability score
def matchResults(definition):
    matches = []
    for i in range(0,len(definition)):
        for j in range(0,len(definition[i])):
            matchContext = {}
            score = sentenceLGPReadabilityScore(definition[i][j])
            matchContext[definition[i][j]] = score
        matches.append(matchContext)
    return matches

# Get LGP sign data of a word
def signData(word):
    queryDB = DBQuery()
    signData = dict(queryDB.select_sign_by_word(word))
    # sign = (id, word, moments, configs, facialExp, hands)
    return signData

# Calculate the LGP readability score of a sign
def wordLGPReadabilityScore(signData):
    formula = LGPFormula()
    score = formula.readability(sign['configs'], sign['moments'], sign['hands'], sign['facialExp'])
    return score

# Calculate the LGP readability score of a sentence
def sentenceLGPReadabilityScore(sentence):
    sentenceScore = 0
    for word in sentence.split(' '):
        if len(word) > 1:
            sign = signData(word)
            sentenceScore += wordLGPReadabilityScore(sign)
    return sentenceScore

# Sort a dictionary in ascending order of values
def sortDefinitions(dictionary):
    return sorted(dictionary.values(), key=lambda x: x[1])


def buildResponse(expression, definition):
    priberam = "https://dicionario.priberam.org/" + expression
    infopedia = "https://www.infopedia.pt/dicionarios/lingua-portuguesa/" + expression
    lexico = "https://www.lexico.pt/" + expression
    wikipedia = "https://pt.wikipedia.org/wiki/" + expression
    info = [ infopedia, lexico, wikipedia]
    response = {'expression' : expression.capitalize(),
                'definition' : definition,
                'source' : priberam,
                'additionalInfo' : info}
    return response

if __name__ == "__main__":
    app.run(debug=True)
