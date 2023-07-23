import pytest
import requests
import  sys


def test1():

    response = app.test_client().get('/bookapi/books/1')
    res = json.loads(response.data.decode('utf-8')).get("Book")

    # letter = 'A'
    # word = 'Alfa'
    # response = requests.get(f'http://127.0.0.1:5000/letter/{letter}')
    # server_response = response.content
    # answer = word.encode('utf-8')
    # assert server_response == answer

