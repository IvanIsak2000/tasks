from alphabet import alphabet
from flask import Flask, request

app = Flask(__name__)


@app.route('/letters/')
def get_alphabet():
    limit = request.args.get('limit')
    offset = request.args.get('offset')
    sort = request.args.get('sort')

    letters = list(map(str.lower, alphabet))

    try:
        limit = int(limit)
    except TypeError or ValueError:
        limit = False

    try:
        offset = int(offset)
    except TypeError or ValueError:
        offset = False

    if sort == 'desc':
        letters = letters[::-1]

    if not limit and not offset:
        return ''.join(letters)

    if limit and not offset:
        return ''.join(letters[:limit])

    if offset and not limit:
        return ''.join(letters[offset:])

    if limit and offset:
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
    return letters


if __name__ == '__main__':
    app.run(debug=True)
