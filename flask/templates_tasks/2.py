from flask import Flask, render_template

app = Flask(__name__)


airport = {
    'code': 'LHR',
    'name': 'Heathrow',
    'runways': 2,
    'country': 'Великобритания',
    'city': 'Лондон'
}


@app.route('/')
def get_airport():
    return render_template('2.html',
                           airport=airport['name'],
                           city=airport['city'],
                           code=airport['code'],
                           runways=airport['runways']
                           )


if __name__ == '__main__':
    app.run(debug=True)
