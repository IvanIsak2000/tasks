from flask import Flask, request

app = Flask(__name__)

users: list[dict[str]] = [
    {"name": "alex", "phone": "+123456789"},
    {"name": "mary", "phone": "+987654321"}
]


@app.route('/', methods=['POST'])
def valid_is_data():
    bad_result: list[str] = []

    name = request.args.get('name')
    phone = request.args.get('phone')

    if name is None:
        bad_result.append('name missed')

    if phone is None:
        bad_result.append('phone missed')

    if not bad_result:
        user = {'name': name, 'phone': phone}
        users.append(user)
        return user

    return bad_result, 400


if __name__ == '__main__':
    app.run(debug=True)
