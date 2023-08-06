from flask import Flask, request

app = Flask(__name__)

from alphabet import alphabet

@app.route('/check/<letter>/<word>')
def equals(letter, word):
    return  str(alphabet[letter.upper()] == word.title())