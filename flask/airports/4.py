from flask import Flask
from flights import all_flights

app = Flask(__name__)


@app.route('/flights/from=<go_from>')
def get_go_from_flights(go_from: str):
    go_from = go_from.upper()
    return [flight.number for flight in all_flights if flight.go_from == go_from]


@app.route('/flights/from/<go_from>/to/<go_to>')
def get_go_from_and_go_to_flights(go_from: str, go_to: str):
    go_from = go_from.upper()
    go_to = go_to.upper()

    return [flight.number for flight in all_flights \
            if flight.go_from == go_from and flight.go_to == go_to]


if __name__ == '__main__':
    app.run(debug=True)
