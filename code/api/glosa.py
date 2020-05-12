from flask import Flask, request

app = Flask(__name__)

@app.route('/convert')
def convert():
    phrase = request.args.get('phrase')
    return phrase

if __name__ == "__main__":
    app.run(debug=True, port=5001)
