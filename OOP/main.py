from abc import ABC, abstractmethod


class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code



class Employee(ABC):
    _departament = None

    def __init__(self, code, name, salary):
        self.code = code
        self.name = name
        self.salary = salary

    @abstractmethod
    def calc_bonus(self):
        pass

    def get_departament(self):
        return self._departament.name

    def set_departament(self, departament_name):
        self._departament.name = departament_name

    @staticmethod
    def get_hours(self):
        return 8    


class Manager(Employee):
    _departament = Department('managers', 1)

    def calc_bonus(self):
        return self.salary * 0.15


class Seller(Employee):
    _departament = Department('sellers', 2)
    _sales = 0

    def calc_bonus(self):
        return self._sales * 0.15

    def get_sales(self):
        return self._sales

    def put_sales(self, valor):
        self._sales += valor
