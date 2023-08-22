from flask import Flask, request
from dataclasses import dataclass

app = Flask(__name__)

users: list[dict[str]] = [
    {"pk": 1, "name": "alex", "phone": "+123456789"},
    {"pk": 2, "name": "mary", "phone": "+987654321"}
]

pk: int = users[-1]['pk']


@dataclass
class User:
    pk: int
    name: str
    phone: str


@app.route('/', methods=['POST'])
def add_item():
    global pk
    pk += 1
    user = User(pk=pk, name=request.args.get('name'), phone=request.args.get('phone'))
    users.append(user)
    return users


if __name__ == '__main__':
    app.run(debug=True)
