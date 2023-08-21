from flask import Flask, request
from flights import all_flights

app = Flask(__name__)


@app.route('/flights/')
def get_numbers():
    go_from = request.args.get('go_from').upper()
    go_to = request.args.get('go_to').upper()

    result = [flight.number for flight in all_flights if flight.go_from == go_from and flight.go_to == go_to]
    return result


if __name__ == '__main__':
    app.run(debug=True)
