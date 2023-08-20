from alphabet import alphabet

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/between/')
def between():
    start_letter = request.args.get('from').upper()
    end_letter = request.args.get('to').upper()

    if start_letter != end_letter:

        start_index = list(alphabet).index(start_letter)
        end_index = list(alphabet).index(end_letter)

        if not start_index < end_index:
            letters = list(alphabet)[end_index + 1:start_index]
            return ''.join(letters)

        letters = list(alphabet)[start_index + 1:end_index]
        return ''.join(letters)

    return '-'


if __name__ == '__main__':
    app.run(debug=True)
