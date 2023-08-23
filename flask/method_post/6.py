from flask import Flask, request

app = Flask(__name__)

users = [
    {"name": "alex", "phone": "+123456789"},
    {"name": "mary", "phone": "+987654321"}
]


@app.route('/', methods=['POST'])
def get_items_len():
    name = request.args.get('name')
    phone = request.args.get('phone')

    users.append({'name': name, 'phone': phone})

    return {'users_count': len(users)}


if __name__ == '__main__':
    app.run(debug=True)
