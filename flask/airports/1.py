from flask import Flask
from flights import all_flights

app = Flask(__name__)


@app.route('/flights/from/<go_from>')
def get_flights(go_from: str):
    go_from = go_from.upper()
    result = [flight.number for flight in all_flights if flight.go_from == go_from]
    return result


if __name__ == '__main__':
    app.run(debug=True)
