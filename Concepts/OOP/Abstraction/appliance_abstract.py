"""
2 ) --
Create an abstract class Appliance with abstract method turn_on().
    Subclasses: WashingMachine, Oven, Fan — each with its own turn_on() message.    
"""
from abc import ABC, abstractmethod

class Appliance(ABC):
    @abstractmethod
    def turn_on(self) -> str:
        return f"{self.__class__.__name__} is turning on..."
    def __repr__(self) -> str:
        return f"A special {self.__class__.__name__}"
class WashingMachine(Appliance):
    def __init__(self, mode : str) -> None:
        self._mode = mode
    def turn_on(self) -> str:
        return super().turn_on() + f", with a mode of {self._mode}"
    def __repr__(self) -> str:
        return super().__repr__() + f"\nMode: {self._mode}"
class Oven(Appliance):
    # time is in minutes
    def __init__(self, time : float) -> None:
        self._time = time
    def turn_on(self) -> str:
        return super().turn_on() + f", with a time of {self._time} minutes" 
    def __repr__(self) -> str:
        return super().__repr__() +f"\nTime: {self._time} minutes"
class Fan(Appliance):
    def __init__(self, mode : str) -> None:
        self._mode = mode
    def turn_on(self) -> str:
        return super().turn_on() + f", on mode of {self._mode}" 
    def __repr__(self) -> str:
        return super().__repr__() + f"\nMode: {self._mode}"
def main():
    washingMachine = WashingMachine("Full")
    oven = Oven(10.5)
    fan = Fan("Fast")
    #  oven.turn_on()
    print("\n".join(machine.turn_on() for machine in [washingMachine, oven, fan]))

if __name__ == "__main__":
    main()