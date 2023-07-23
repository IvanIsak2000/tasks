from alphabet import alphabet

from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/get/')
def get_len():
    len_ = int(request.args.get('len'))
    result = []

    if len_ > 3:
        words = list(dict(alphabet).values())
        for w in words:
            if len(w)  == len_:
                result.append(w)

        return ' '.join(result)

    return abort(404)
