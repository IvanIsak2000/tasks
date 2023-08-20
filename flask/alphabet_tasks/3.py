from flask import Flask, request
from alphabet import alphabet

app = Flask(__name__)


@app.route('/check/<letter>/<word>')
def equals(letter, word):
    return str(alphabet[letter.upper()] == word.title())


if __name__ == '__main__':
    app.run(debug=True)
