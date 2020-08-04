from flask import Flask, jsonify, request
from flask_cors import CORS
from webscraping.ws_priberam import Priberam
from db.querydb import *

app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def index():
    return "Hello World!"

@app.route('/search')
def search():
    expression = request.args.get('query')
    if(expression != ""):
        priberam = "https://dicionario.priberam.org/" + expression
        infopedia = "https://www.infopedia.pt/dicionarios/lingua-portuguesa/" + expression
        lexico = "https://www.lexico.pt/" + expression
        wikipedia = "https://pt.wikipedia.org/wiki/" + expression
        info = [ infopedia, lexico, wikipedia]
        definition = Priberam.scrap(expression)
        response_object = {'expression' : expression.capitalize(),
            'definition' : definition,
            'source' : priberam,
            'additionalInfo' : info}
    else:
        response_object = None
    return jsonify(response_object)

def testWord(word):
    database = "db/pythonsqlite.db"
    conn = create_connection(database)
    row = select_pt_sign_by_word(conn, word)

if __name__ == "__main__":
    app.run(debug=True)
