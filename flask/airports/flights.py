from dataclasses import dataclass


@dataclass
class Flight:
    number: str  # номер рейса
    carrier: str  # авиакомпания
    plane: str  # самолет
    go_from: str  # аэропорт вылета
    go_to: str  # аэропорт прибытия


all_flights = [
    Flight(
        number="AF123",
        carrier="Aeroflot",
        plane="Boeing737",
        go_from="DME",
        go_to="HEL"
    ), Flight(
        number="UA300",
        carrier="Ural Airlines",
        plane="Embraer170",
        go_from="HEL",
        go_to="DME"
    ), Flight(
        number="CD456",
        carrier="S7 Airlines",
        plane="AirbusA320",
        go_from="LEN",
        go_to="DME"
    ), Flight(
        number="EF789",
        carrier="Ural Airlines",
        plane="AirbusA321",
        go_from="SVX",
        go_to="AER"
    ), Flight(
        number="GH012",
        carrier="Pobeda",
        plane="Boeing737",
        go_from="DME",
        go_to="AER"
    ), Flight(
        number="IJ345",
        carrier="Aeroflot",
        plane="Boeing777",
        go_from="HEL",
        go_to="DME"
    )]
