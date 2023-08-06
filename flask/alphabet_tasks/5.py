from alphabet import alphabet

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/get_some/<number>')
def get_some(number):
    '''у автора ошибка: он говорит что мол при подаче числа 3 должно вернуть 2 числа, но это не так -
    сколько цифр - столько букв, значит автор забыл С в примере дописать!'''

    if number != 0:
        letters = list(alphabet)[0:int(number)]
        return ''.join(letters)
    return '-'