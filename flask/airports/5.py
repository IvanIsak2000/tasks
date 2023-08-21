from flask import Flask, request
from flights import all_flights

app = Flask(__name__)


@app.route('/flights/')
def get_flights_numbers():
    planes = request.args.get('with')
    return [flight.number for flight in all_flights if flight.plane in planes]


if __name__ == '__main__':
    app.run(debug=True)
