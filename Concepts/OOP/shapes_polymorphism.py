"""
    Exercise 2
Make a base class Shape with a method area().
Subclasses: Rectangle, Triangle, Circle.
Each calculates its own area differently.
"""
import math

class Shape():
    def __init__(self, base : float, height : float) -> None:
        self._base = base
        self._height = height
    def area(self) -> float:
        return self._base * self._height
    def __repr__(self) -> str:
        return f"Base: {self._base} Height: {self._height}"
    def perimeter(self) -> float:
        return (self._base * 2) + (self._height * 2) 
class Rectangle(Shape):
    def __init__(self, base: float, height: float) -> None:
        super().__init__(base, height)
    def area(self) -> float:
        return super().area()
    def perimeter(self) -> float:
        return super().perimeter()
class Triangle(Shape):
    def __init__(self, base: float, height: float, side_1 : float, side_2 :float) -> None:
        super().__init__(base, height)
        self._side_1 = side_1
        self._side_2 = side_2
    def area(self) -> float:
        return float(super().area()) / 2
    def perimeter(self) -> float:
        return self._base + self._side_1 + self._side_2
class Circle(Shape):
    # In this case the circle's radio is like a base
    def __init__(self, base: float, height=None) -> None:
        super().__init__(base, height)
    def area(self) -> float:
        return (self._base ** 2) * math.pi
    def perimeter(self) -> float:
        return 2 * self._base * math.pi
def main():
    shape = Shape(23, 33)
    rectangle = Rectangle(80, 60)
    triangle = Triangle(20, 15, 10, 10)
    circle = Circle(19)
    for shapes in [shape, rectangle, triangle, circle]:
        print(f"the area is: {shapes.area()}")
        print(f"the perimeter is: {shapes.perimeter()}")
if __name__ == "__main__":
    main()
    
    