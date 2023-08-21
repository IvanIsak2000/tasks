from flask import Flask
from flights import all_flights

app = Flask(__name__)


@app.route('/flights/between/<go_from>-<go_to>')
def get_flights_between(go_from, go_to):
    go_from = go_from.upper()
    go_to = go_to.upper()

    result_from = [flight.number for flight in all_flights \
                   if flight.go_from == go_from and flight.go_to == go_to]

    result_to = [flight.number for flight in all_flights \
                 if flight.go_from == go_to and flight.go_to == go_from]

    return result_from + result_to


if __name__ == '__main__':
    app.run(debug=True)
