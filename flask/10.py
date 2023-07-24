from alphabet import alphabet
from flask import Flask, request, abort
app = Flask(__name__)


@app.route('/letters/')
def get_alphabet():
    limit = request.args.get('limit')
    offset = request.args.get('offset')
    sort = request.args.get('sort')

    letters = list(alphabet)
    letters = list(map(str.lower, alphabet))

    try:
        limit = int(limit)
        offset = int(offset)
    except ValueError:
        pass

    if sort == 'desc':
        letters = letters[::-1]

    if limit is None and offset is None:
        return ''.join(letters)

    if limit is not None and offset is None:
        return ''.join(letters[:limit])

    if offset is not None and limit is None:
        return ''.join(letters[limit:])

    if limit is not None and offset is not None:
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
