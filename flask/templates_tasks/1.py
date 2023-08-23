from flask import Flask, render_template

app = Flask(__name__)

# Данные для шаблона:

flight_number = 'SU123'
aircraft = 'Airbus A320'

departure_time = '14:30'
arrival_time = '18:45'

departure_airport = 'SVO'
arrival_airport = 'JFK'


@app.route('/')
def get_flight():
    return render_template('1.html',
                           departure_airport=departure_airport,
                           arrival_airport=arrival_airport,
                           departure_time=departure_time,
                           arrival_time=arrival_time
                           )


if __name__ == '__main__':
    app.run(debug=True)
