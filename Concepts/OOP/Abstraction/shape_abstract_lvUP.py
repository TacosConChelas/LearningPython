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
        return (
            f"---- {self.__class__.__name__} ----:\n"
            f"Area = {round(self.area(), 2)}, Perimeter = {round(self.perimeter(), 2)}"
            )
class Circle(Shape):
    def __init__(self, radius : float) -> None:
        self._radius = radius
    def area(self) -> float:
        return (self._radius ** 2) * math.pi
    def perimeter(self) -> float:
        return 2 * math.pi * self._radius
    def __repr__(self) -> str:
        return super().__repr__() + f"\nRadius = {round(self._radius, 2)}"
class Triangle(Shape):
    def __init__(self, base : float, side_1 : float, side_2 : float, height : float) -> None:
        self._base = base
        self._side_1 = side_1
        self._side_2 = side_2
        self._height = height
    def area(self) -> float:
        return (self._base * self._height) / 2
    def perimeter(self) -> float:
        return self._base + self._side_1 + self._side_2
    def __repr__(self) -> str:
        return (
            super().__repr__() + f"\nBase = {round(self._base, 2)}, Height = {round(self._height, 2)},"
            f" Side 1 = {round(self._side_1, 2)}, Side 2 = {round(self._side_2, 2)}"
            )    
class Rectangle(Shape):
    def __init__(self, base : float, height : float) -> None:
        self._base = base
        self._height = height
    def area(self) -> float:
        return self._base * self._height
    def perimeter(self) -> float:
        return (self._base * 2) + (self._height * 2)
    def __repr__(self) -> str:
        return (super().__repr__() + f"\nBase = {round(self._base)}, Height = {round(self._height, 2)}")

def main():
    triangle = Triangle(20, 10, 10, 15)
    circle = Circle(20)
    rectangle = Rectangle(30, 15)

    for shape in [triangle, circle, rectangle]:
        print(shape)
if __name__ == "__main__":
    main()

