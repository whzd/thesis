from flask import Flask, jsonify, request
from flask_cors import CORS
from webscraping.ws_priberam import Priberam

app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def index():
    return "Hello World!"

@app.route('/search')
def search():
    expression = request.args.get('query')
    print(expression)
    if(expression != ""):
        priberam = "https://dicionario.priberam.org/" + expression
        infopedia = "https://www.infopedia.pt/dicionarios/lingua-portuguesa/" + expression
        lexico = "https://www.lexico.pt/" + expression
        sources = [ priberam, infopedia, lexico ]
        definition = Priberam.scrap(expression)
        response_object = {'expression' : expression,
            'definition' : definition,
            'sources' : sources }
    else:
        response_object = None
    return jsonify(response_object)

@app.route('/concept', methods=['POST'])
def explanation():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        return jsonify(response_object)

if __name__ == "__main__":
    app.run(debug=True)