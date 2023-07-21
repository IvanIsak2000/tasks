from alphabet import alphabet

from flask import Flask, request, render_template, abort

app = Flask(__name__)

@app.route('/')
def home():
    letters = list(alphabet)[:5]
    print(letters)
    return ''.join(map(str.lower, letters))

@app.route('/page/<number>')
def number(number):
    if int(number) <= 5: 
        letters = list(map(str.lower,list(alphabet)))

        by_5 = []
        first_absolutly_posit = 0
        second_absolutly_posit = 5 

        limit = 5

        while limit!=0:
            by_5.append(list(letters)[first_absolutly_posit:second_absolutly_posit])

            first_absolutly_posit += 5
            second_absolutly_posit += 5
            limit -=1

        print(type(by_5))
        return ''.join(list(by_5)[int(number)-1])
    return abort(404)




