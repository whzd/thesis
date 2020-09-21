import unidecode
import string
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
        # sort results based on LGP readability
        sort = False
        resultsScores = matchResults(definitions, sort)

        #5. Present the definition with the highest number of matches
        response_object = buildResponse(expression, definitions)

    else:
        response_object = None
    return jsonify(response_object)

# Create a dictionary of results orders by LGP readability score
def matchResults(definition, sort):
    # All results
    matches = []
    # Results
    for i in range(0,len(definition)):
        # Context results
        matchContext = []
        # Single result
        explScore = {}
        # Each context
        for j in range(0,len(definition[i])):
            score = sentenceLGPReadabilityScore(definition[i][j])
            explScore[definition[i][j]] = score
        # Sort context explanation
        if sort:
            matchContext.append(sortDefinitions(explScore))
        else:
            matchContext.append(explScore)
        matches.append(matchContext)
    return matches

# Get the LGP sign data for each char of a word
def listOfChar(queryDB, word):
    simpleWord = unidecode.unidecode(word)
    upperCaseWord = simpleWord.upper()
    signData = []
    for char in upperCaseWord:
        signData.append(dict(queryDB.select_sign_by_word(char)))
    return signData

# Get LGP sign data of a word
def signData(word):
    queryDB = DBQuery()
    queryResult = queryDB.select_sign_by_word(word)
    if queryResult == None:
        signData = listOfChar(queryDB, word)
    else:
        signData = dict(queryResult)
    # sign = (id, word, moments, configs, facialExp, hands)
    return signData

# Calculate the LGP readability score of a sign
def wordLGPReadabilityScore(signData):
    formula = LGPFormula()
    score = formula.readability(signData['configs'], signData['moments'], signData['hands'], signData['facialExp'])
    return score

# Calculate the LGP readability score of a sentence
def sentenceLGPReadabilityScore(sentence):
    sentenceScore = 0
    numberOfWords = 0
    for word in sentence.split(' '):
        # Removes ponctuation
        simpleWord = word.translate(str.maketrans('', '', string.punctuation))
        if len(simpleWord) > 1:
            numberOfWords += 1
            sign = signData(simpleWord)
            if isinstance(sign, dict):
                sentenceScore += wordLGPReadabilityScore(sign)
            else:
                for letter in sign:
                    sentenceScore += wordLGPReadabilityScore(letter)
    return sentenceScore/numberOfWords

# Sort a dictionary in ascending order of values
def sortDefinitions(dictionary):
    return dict(sorted(dictionary.items(), key=lambda x: x[1]))

# Create response object
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
