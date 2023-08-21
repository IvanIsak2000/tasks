from flask import Flask, request

app = Flask(__name__)

items = ["alpha", "bravo", "charlie"]


@app.route('/', methods=['POST'])
def items_add():
    word = request.args.get('word')
    items.append(word)
    return items


if __name__ == '__main__':
    app.run(debug=True)
