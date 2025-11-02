"""
    Exercise 1
Create: 
    a base class Animal with a method speak().
Subclasses: 
    Dog, Cat, Cow, each printing a different sound.
Loop through all animals and call .speak().
"""
class Animal():
    def __init__(self, color, age, race=None) -> None:
        self._color = color
        self._age = age
        self._race = race   
    def speak(self) -> str:
        return "Any sound"
    def __repr__(self) -> str:
        return f"color: {self._color} Age: {self._age}"
class Cat(Animal):
    def __init__(self, color, age, race=None) -> None:
        super().__init__(color, age, race)
    def speak(self) -> str:
        return "Meou Meou"
    def __repr__(self) -> str:
        return super().__repr__() + f" Race: {self._race}"
class Dog(Animal):
    def __init__(self, color, age, race=None) -> None:
        super().__init__(color, age, race)
    def speak(self) -> str:
        return "Guaf Guaf"
    def __repr__(self) -> str:
        return super().__repr__() + f" Race: {self._race}"
class Cow(Animal):
    def __init__(self, color, age, race=None) -> None:
        super().__init__(color, age, race)
    def speak(self) -> str:
        return "Muuuu Muuuuu"
    def __repr__(self) -> str:
        return super().__repr__() + f" Race: {self._race}"
def main():
    animal = Animal("Red", 23)
    dog = Dog("Black", 7, "daughshot")
    cat = Cat("Black", 6, "litzu")
    cow = Cow("Black and White", 9, "milker")
    for animal in [animal, dog, cat, cow]:
        print(animal.speak())

if __name__ == "__main__":
    main()