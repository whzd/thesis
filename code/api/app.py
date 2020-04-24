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
    strings = []
    expression = request.args.get('query')
    definition1 = Priberam.scrap(expression)
    strings.append(definition1)
    response_object = {'resp' : strings }
    return jsonify(response_object)

@app.route('/concept', methods=['POST'])
def explanation():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        return jsonify(response_object)

if __name__ == "__main__":
    app.run(debug=True)
