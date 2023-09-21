from flask import Flask, render_template

app = Flask(__name__)

ticket = {
    'seat': '12A',
    'class': 'economy',

    'passenger': {
            'name': 'John Smith'
    },

    'aircraft': {
        'model': 'Boeing 737'
    },

    'flight': {
        'departure_time': '10:00',
        'arrival_time': '12:30'
    }
}


@app.route('/', methods=['POST'])
def return_ticket():
    return render_template('4.html',
                       name=ticket['passenger']['name'],
                       seat=ticket['seat'],
                       class_=ticket['class'],
                       aircraft=ticket['aircraft']['model'],
                       departure_time=ticket['flight']['departure_time'],
                       arrival_time=ticket['flight']['arrival_time']
                           )


if __name__ == '__main__':
    app.run(debug=True)
