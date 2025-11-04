"""
4 ) --- 
Create an abstract class Employee with calculate_salary() and get_role().
Subclasses: Manager, Developer, Intern.
"""
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, base_salary : float, role : str, name : str, age : int, number_month : int) -> None:
        super().__init__()
        self._base_salary = base_salary
        self._role = role
        self._name = name
        self._age = age
        self._number_month = number_month
    @abstractmethod 
    def calculate_salary(self) -> float:
        pass
    @abstractmethod
    def get_role(self) -> str:
        pass
    def __repr__(self) -> str:
        return (
            "<_______Employee Info_______>\n"
            f"{self.__class__.__name__}: {self._name}\n"
            f"Role: {self._role}, Salary Deal: {self._base_salary}\n"
            f"# Months: {self._number_month}, Tot Salary: {self.calculate_salary()}"
        )
class Manager(Employee):
    def calculate_salary(self) -> float:
        # depend of the employee is the bonus
        return self._base_salary * self._number_month + 100
    def get_role(self) -> str:
        return f"The {self.__class__.__name__}'s role is {self._role}"
class Developer(Employee):
    def calculate_salary(self) -> float:
        return self._base_salary * self._number_month + 50
    def get_role(self) -> str:
        return f"The {self.__class__.__name__}'s role is {self._role}"
class Intern(Employee):
    def calculate_salary(self) -> float:
        return self._base_salary * self._number_month + 5 
    def get_role(self) -> str:
        return f"The {self.__class__.__name__}'s role is {self._role}"
def main() -> None:
    manager = Manager(2000, "Manager", "Bob", 30, 5)
    developer = Developer(1500, "Developer", "Jose", 28, 6)
    intern = Intern(1000, "Intern", "Jack", 20, 2)
    print("\n".join(f"{employ}" for employ in [manager, developer, intern]))

if __name__ == "__main__":
    main()
