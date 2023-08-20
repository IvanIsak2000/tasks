from alphabet import alphabet

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/letters/')
def offset():
    limit = int(request.args.get('limit'))
    offset = int(request.args.get('offset'))
    letters = list(map(str.lower, alphabet))

    if limit <= 26 and offset < 26:
        answer = []
        i = 0
        while limit > 0:
            try:
                answer.append(letters[offset + i].lower())
            except IndexError:
                break
            i += 1
            limit -= 1
        return ''.join(answer)

    return '-'
