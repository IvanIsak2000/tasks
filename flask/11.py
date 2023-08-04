from flask import Flask, request, render_template
from dataclasses import dataclass

app = Flask(__name__)


@dataclass
class Flight1:
    # number: str
    # carrier: str
    plane: str
    from_: str
    # to: str
    departure_time: str
    arriving_time: str
    # seats: int
    # tickets_sold: int


@dataclass
class Flight2:
    # number: str
    # carrier: str
    plane: str
    # from_: str
    to: str
    departure_time: str
    arriving_time: str
    # seats: int
    # tickets_sold: int
    #


@app.route('/flights/')
def return_flights():
    from_ = request.args.get('from').upper()
    to = request.args.get('to').upper()

    f1 = Flight1(
        from_=from_.upper(),
        plane='AB123',
        departure_time='10:33',
        arriving_time='13:17')

    f2 = Flight2(
        to=to.upper(),
        plane='AB123',
        departure_time='16:05',
        arriving_time='18:55')

    if from_ == to:
        return f'''
            {f1.from_} > {f2.to}
            <br>
            <br>
            Не найдено'''

    return f'''
        {f1.from_} > {f2.to}
        <br>
        <br>
        {f1.plane} {f1.departure_time} > {f1.arriving_time}
        <br>
        {f2.plane} {f2.departure_time} > {f2.arriving_time}
        '''


if __name__ == '__main__':
    app.run()
