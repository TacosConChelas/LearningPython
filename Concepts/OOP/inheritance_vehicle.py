"""
Task:
    Create a base class Vehicle with:
        Attributes: make, model, year
        Method: start() → print(f"{self.make} {self.model} is starting...")
    Then create two subclasses:
        Car(Vehicle) — adds doors attribute and overrides start() to print something custom.
        Motorcycle(Vehicle) — adds cc attribute and overrides start() too.
    Finally, create objects for both and show that inheritance works.
"""
from time import sleep


class Vehicle():
    def __init__(self, make : str, model : str, year : int) -> None:
        self._make = make
        self._model = model
        self._year = year
    
    def start(self):
        print(f"{self._make} {self._model} is starting...")
    

class Car(Vehicle):
    def __init__(self, make: str, model: str, year: int, serial_number : int) -> None:
        super().__init__(make, model, year)
        self._serial_n = serial_number
    
    def start(self) -> None:
        print(f"The car {self._model} with SN: {self._serial_n} is starting...")

class Motorcycle(Vehicle):
    def __init__(self, make: str, model: str, year: int, speed_average : float) -> None:
        super().__init__(make, model, year)
        self._speed_average = speed_average

    def speed(self):
        print(f"The motorcycle {self._model} has a average speed of {self._speed_average}")        

def main():
    car = Car("General Motors", "T-2323", 2004, 6667)
    car.start()

    mcycle = Motorcycle("Takiyaki", "Raptor", 2026, 2000.0)
    mcycle.speed()

if __name__ == "__main__":
    main()