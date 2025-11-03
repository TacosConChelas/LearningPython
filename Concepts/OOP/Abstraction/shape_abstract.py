"""
1 ) ---
Create an abstract class Shape with:
    Abstract method area()
    Abstract method perimeter()
    Subclasses: Circle, Rectangle, and Triangle.
"""
from abc import ABC, abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass

    def __repr__(self) -> str:
        return f"---- {self.__class__.__name__} ----: Area = {self.area()}, Perimeter = {self.perimeter()}"
class Circle(Shape):
    def __init__(self, radius : float) -> None:
        super().__init__()
        self._radius = radius
    def area(self) -> float:
        return (self._radius ** 2) * math.pi
    def perimeter(self) -> float:
        return 2 * math.pi * self._radius
    def __repr__(self) -> str:
        return super().__repr__() + f"\nRadius = {self._radius}"
class Triangle(Shape):
    def __init__(self, base : float, side_1 : float, side_2 : float, height : float) -> None:
        super().__init__()
        self._base = base
        self._side_1 = side_1
        self._side_2 = side_2
        self._height = height
    def area(self) -> float:
        return (self._base * self._height) / 2
    def perimeter(self) -> float:
        return self._base + self._side_1 + self._side_2
    def __repr__(self) -> str:
        return super().__repr__() + f"\nBase = {self._base} Height = {self._height} Side 1 = {self._side_1} Side 2 = {self._side_2}"    
class Rectangle(Shape):
    def __init__(self, base : float, height : float) -> None:
        super().__init__()
        self._base = base
        self._height = height
    def area(self) -> float:
        return self._base * self._height
    def perimeter(self) -> float:
        return (self._base * 2) + (self._height * 2)
    def __repr__(self) -> str:
        return super().__repr__() + f"\nBase = {self._base} Height = {self._height}"

def main():
    triangle = Triangle(20, 10, 10, 15)
    circle = Circle(20)
    rectangle = Rectangle(30, 15)

    for shape in [triangle, circle, rectangle]:
        print(shape.__repr__())
if __name__ == "__main__":
    main()

