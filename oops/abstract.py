from abc import ABC, abstractmethod

class Vehical(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehical):
    def go(self):
        print("car left")

    def stop(self):
        print("car stoped")

car = Car()


car.go()
car.stop()