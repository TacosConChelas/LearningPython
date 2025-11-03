"""
2 ) --
Create an abstract class Appliance with abstract method turn_on().
    Subclasses: WashingMachine, Oven, Fan — each with its own turn_on() message.    
"""
from abc import ABC, abstractmethod
import string

class Appliance(ABC):
    @abstractmethod
    def turn_on(self) -> str:
        return f"{self.__class__.__name__} is turning on..."
    def __repr__(self) -> str:
        return f"A special {self.__class__.__name__}"
class WashingMachine(Appliance):
    def __init__(self, speed : float) -> None:
        self._speed = speed
    def turn_on(self) -> str:
        return super().turn_on() + f", with a speed of {self._speed}"
    def __repr__(self) -> str:
        return super().__repr__() + f"\nSpeed: {self._speed}"
class Oven(Appliance):
    def __init__(self, time : float) -> None:
        self._time = time
    def turn_on(self) -> str:
        return super().turn_on() + f", with a time of {self._time} minutes" 
    def __repr__(self) -> str:
        return super().__repr__() + f"\nTime: {self._time} minutes" 