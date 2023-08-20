from alphabet import alphabet

from flask import Flask, request, abort

app = Flask(__name__)


@app.route('/search/')
def subtitle():
    """автор походу забыл указать и BRAvo в которой содердтся подстрока ra"""

    subtitle = request.args.get('s')

    letters = list(dict(alphabet).values())
    letters = list(map(str.lower, letters))

    result = []

    for l in letters:
        if subtitle in l:
            result.append(l.title())

    if not result:
        return abort(404)

    return ', '.join(result)


if __name__ == '__main__':
    app.run(debug=True)
