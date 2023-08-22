from flask import Flask, request

app = Flask(__name__)

x = 0  # default start value


@app.route('/', methods=['POST'])
def get_x_plus_one():
    global x
    x += 1
    return str(x)


if __name__ == '__main__':
    app.run(debug=True)
