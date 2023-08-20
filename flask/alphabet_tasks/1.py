from flask import Flask
from alphabet import alphabet

app = Flask(__name__)


@app.route('/letter/<letter>')
def return_letter(letter):
    return alphabet[letter]


if __name__ == '__main__':
    app.run(debug=True)
