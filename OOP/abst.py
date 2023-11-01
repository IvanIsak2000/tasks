from abc import ABC, abstractmethod 

class Venicle(ABC):
    @abstractmethod
    def start(self):
        self

    @abstractmethod
    def stop(self):
        self

class Airplane(Venicle):
    def start(self):
        print('the airplane was start')

    def stop(self):
        print('the airplane was stop')

# venicle = Venicle()
airplane = Airplane()

airplane.start()