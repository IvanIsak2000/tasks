from flask import Flask, request
from alphabet import alphabet

app = Flask(__name__)


@app.route('/find/')
def find_letter():
    letter = request.args.get('letter').upper()
    return alphabet[letter]


if __name__ == '__main__':
    app.run(debug=True)
