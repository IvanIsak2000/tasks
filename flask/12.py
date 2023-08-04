from flask import Flask
from dataclasses import dataclass
from airports import airports

app = Flask(__name__)


@dataclass
class Flight1:
    # number: str
    # carrier: str
    plane: str
    from_: str
    to: str
    departure_time: str
    arriving_time: str
    # seats: int
    # tickets_sold: int


@dataclass
class Flight2:
    # number: str
    # carrier: str
    plane: str
    from_: str
    to: str
    departure_time: str
    arriving_time: str
    # seats: int
    # tickets_sold: int
    #

@app.route('/flights/between/<from_>&<to>')
def get_flights(from_, to):
    f1 = Flight1(
        from_=from_.upper(),
        to=to.upper(),
        plane='AB123',
        departure_time='10:33',
        arriving_time='13:17'
    )

    f2 = Flight2(
        from_=to.upper(),
        to=from_.upper(),
        plane='AB123',
        departure_time='16:05',
        arriving_time='18:55'
    )

    if f1.from_ == f1.to:
        return 'Не найдено'

    if f1.from_ not in airports or f1.to not in airports:
        print(airports)
        return 'Таких аэропортов нет'

    f1_index = airports.index(f1.from_)
    f2_index = airports.index(f1.to)
    if f2_index - f1_index == 1:
        return f'''
            {f1.from_} <> {f2.from_}
            <br>
            <br>
            {f1.plane} {f1.from_} {f1.departure_time} > {f1.arriving_time} {f1.to}
            <br>
            {f2.plane} {f2.from_} {f2.departure_time} > {f2.arriving_time} {f2.to}
            '''

if __name__ == '__main__':
    app.run(debug=True)