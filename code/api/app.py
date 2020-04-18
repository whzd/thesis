from flask import Flask, jsonigy, request

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World!"

@app.route('/concept', methods=['POST'])
def explanation():
    response_object = {'status': 'success'}
    if request.method == 'POST':
    return jsonify(response_object)

if __name__ == "__main__":
    app.run(debug=True)
