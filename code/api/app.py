from flask import Flask, jsonify, request
from flask_cors import CORS
from webscraping.ws_priberam import Priberam
from db.querydb import create_connection, check_pt_number_of_words

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
        sortedMatchList = buildWordMatchList(definitions)

        #5. Present the definition with the highest number of matches
        response_object = buildResponse(expression, definition)

    else:
        response_object = None
    return jsonify(response_object)

def buildSortedMatchList(definitions):
    matches = []
    res = []
    for i in len(definitions):
        for j in len(definitions[i]):
            numberOfWords = testSentence(definitions[i][j])
            matches.append(numberOfWords)
        res.append([x for _,x in sorted(zip(matches,definitions[i]))])
        matches.clear()
    return res

def testSentence(sentence):
    database = "db/pythonsqlite.db"
    conn = create_connection(database)
    res = check_pt_number_of_words(conn, sentence)
    return res

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
