from flask import Flask, request

app = Flask(__name__)

enrollments = [
    {"name": "alex", "phone": "+123456789"},
]


@app.route('/', methods=['POST'])
def add_item():
    name = request.args.get('name')
    phone = request.args.get('phone')

    new_item = {'name': name, 'phone': phone}
    enrollments.append(new_item)
    return enrollments


if __name__ == '__main__':
    app.run(debug=True)


