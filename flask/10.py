from alphabet import alphabet

from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/letters/')
def get_alphabet():
    limit = request.args.get('limit')
    offset = request.args.get('offset')
    sort = request.args.get('sort')

    letters = list(alphabet)
    letters = list(map(str.lower, alphabet))

    if sort == 'desc':
        letters = letters.reverse()

    if limit == None and offset == None:
        return ''.join(letters)

    if limit != None and offset == None:
        return ''.join(letters[:int(limit)])

    if offset != None and limit == None:
        return ''.join(letters[int(limit):])

    if limit != None and offset != None:
        return 

    return letters




    # if limit <= 26 and offset <26:
    #     start_letter = list(alphabet)[offset]
    #     answer = []
    #     i=0
    #     while limit>0:
    #         try:
    #             answer.append(list(alphabet)[offset+i]).lower()
    #         except IndexError:
    #             break
    #         i+=1
    #         limit -=1
    #     return answer

