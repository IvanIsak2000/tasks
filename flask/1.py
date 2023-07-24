from flask import Flask, render_template

app = Flask(__name__)

from alphabet import alphabet

@app.route('/letter/<letter>')
def return_letter(letter):
    return alphabet[letter]