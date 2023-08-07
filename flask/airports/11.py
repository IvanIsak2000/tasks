from dataclasses import dataclass
from flask import Flask, jsonify	from flask import Flask, jsonify
app = Flask(__name__)	app = Flask(__name__)
@dataclass	@dataclass
class Flight:	class Flight:
    number: str  # номер рейса	    number: str  # номер рейса
    carrier: str  # авиакомпания	    carrier: str  # авиакомпания
    plane: str  # самолет	    plane: str  # самолет
    go_from: str  # аэропорт вылета	    go_from: str  # аэропорт вылета
    go_to: str  # аэропорт прибытия	    go_to: str  # аэропорт прибытия
all_flights = [	all_flights = [
  Flight(	  Flight(
    number="AF123", 	    number="AF123", 
    carrier="Aeroflot", 	    carrier="Aeroflot", 
    plane="Boeing737", 	    plane="Boeing737", 
    go_from="DME", 	    go_from="DME", 
    go_to="HEL"	    go_to="HEL"
  ), Flight(	  ), Flight(
    number="UA300", 	    number="UA300", 
    carrier="Ural Airlines", 	    carrier="Ural Airlines", 
    plane="Embraer170", 	    plane="Embraer170", 
    go_from="HEL", 	    go_from="HEL", 
    go_to="DME"	    go_to="DME"
  ), Flight(	  ), Flight(
    number="CD456", 	    number="CD456", 
    carrier="S7 Airlines", 	    carrier="S7 Airlines", 
    plane="AirbusA320", 	    plane="AirbusA320", 
    go_from="LEN", 	    go_from="LEN", 
    go_to="DME"	    go_to="DME"
), Flight(	), Flight(
    number="EF789", 	    number="EF789", 
    carrier="Ural Airlines", 	    carrier="Ural Airlines", 
    plane="AirbusA321", 	    plane="AirbusA321", 
    go_from="SVX", 	    go_from="SVX", 
    go_to="AER"	    go_to="AER"
), Flight(	), Flight(
    number="GH012", 	    number="GH012", 
    carrier="Pobeda", 	    carrier="Pobeda", 
    plane="Boeing737", 	    plane="Boeing737", 
    go_from="DME", 	    go_from="DME", 
    go_to="AER"	    go_to="AER"
), Flight(	), Flight(
    number="IJ345", 	    number="IJ345", 
    carrier="Aeroflot", 	    carrier="Aeroflot", 
    plane="Boeing777", 	    plane="Boeing777", 
    go_from="HEL", 	    go_from="HEL", 
    go_to="DME"	    go_to="DME"
)]	)]
@app.route('/flights/from/<from_>')	@app.route('/flights/from/<from_>')
def get_flighs(from_: str):	def get_flighs(from_: str):
    airport = from_.upper()	    airport = from_.upper()


    valid_airports = []	    # solution 1 
    for i in range(len(all_flights)):	    # valid_airports = []
        if all_flights[i].go_from == airport:	    # for i in range(len(all_flights)):
            valid_airports.append(all_flights[i].number)	    #     if all_flights[i].go_from == airport:
    return sorted(valid_airports)	    #         valid_airports.append(all_flights[i].number)
    # return sorted(valid_airports)


    # result = [flight.number for flight in  all_flights if all_flights.go_from == airport ]	    # one-line solution
    # return jsonify(result)	    result = [flight.number for flight in  all_flights if flight.go_from == airport ]
    return jsonify(result)




if __name__ == '__main__':	if __name__ == '__main__':
    app.run(debug=True)	    app.run(debug=True)
