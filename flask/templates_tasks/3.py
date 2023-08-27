from flask import Flask, render_template

app = Flask(__name__)

aircraft = {
    'model': 'Airbus A380',
    'year': 2007,
    'crew': 3,
    'airline': {
        'name': 'Emirates',
        'country': 'ОАЭ'
    }
}

@app.route('/')
def get_template():
    return render_template('3.html',
                           model=aircraft['model'],
                           name=aircraft['airline']['name'],
                           country=aircraft['airline']['country']
                           )


if __name__ == '__main__':
    app.run(debug=True)
