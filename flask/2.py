from flask import Flask, render_template, request

app = Flask(__name__)

from alphabet import alphabet

@app.route('/find/')
def find_letter():
    letter = request.args.get('letter').upper()
    return alphabet[letter]