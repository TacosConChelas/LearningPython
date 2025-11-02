"""
    Exercise 1
Create: 
    a base class Animal with a method speak().
Subclasses: 
    Dog, Cat, Cow, each printing a different sound.
Loop through all animals and call .speak().
"""
class Animal():
    def __init__(self, color, age) -> None:
        self._color = color
        self._age = age
    
    def speak(self) -> str:
        return "Any sound"


