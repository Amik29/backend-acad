import math
class Circle:

    def __init__(self, radius:float = 0.):
        self.__radius = float(radius)

    def setRadius(self,radius:float):
        self.__radius = float(radius);

    def getRadius(self):
        return self.__radius

    def getArea(self):
        return (self.__radius**2)*math.pi
    
    def getPerimeter(self):
        return 2*math.pi*self.__radius
    
print("Задание 1:")
rect1 = Circle(10)
print(f'Radius: {rect1.getRadius()}, Perimeter: {rect1.getPerimeter()}, Area: {rect1.getArea()}')
rect1.setRadius(15)
print(f'Radius: {rect1.getRadius()}, Perimeter: {rect1.getPerimeter()}, Area: {rect1.getArea()}')
print("======================")

print("Задание 2:")
from datetime import datetime
class Human:
    def __init__(self,name:str,city:str,birth:datetime):
        self.name = name
        self.city = city
        self.birth = birth
    
    def getAge(self):
        day_difference = (datetime.now() - self.birth).days % 365 == 0
        return datetime.now().year - self.birth.year - day_difference
    
    def __str__(self):
        return f'{self.name} : {self.birth} in {self.city}'

human1 = Human("Петр","Уфа",datetime(1990,4,21))
print(human1.getAge())
print("======================")

print("Задание 3:")
class NumberException:
    pass

class Calculator:
    def __init__(self) -> None:
        pass
    
    def add(lhs,rhs):
        if (isinstance(lhs,(int,float)) and isinstance(rhs,(int,float))):
            return lhs+rhs
        else:
            raise NumberException("Lhs and rhs must be int or float!")
    def substract(lhs,rhs):
        if (isinstance(lhs,(int,float)) and isinstance(rhs,(int,float))):
            return lhs-rhs
        else:
            raise NumberException("Lhs and rhs must be int or float!")
    def multuply(lhs,rhs):
        if (isinstance(lhs,(int,float)) and isinstance(rhs,(int,float))):
            return lhs*rhs
        else:
            raise NumberException("Lhs and rhs must be int or float!")
    
    def division(lhs,rhs):
        if (isinstance(lhs,(int,float)) and isinstance(rhs,(int,float))):
            try:
                return lhs/rhs
            except ZeroDivisionError:
                print("Devided by zero")
                return 0
        else:
            raise NumberException("Lhs and rhs must be int or float!")

calc = Calculator
print(calc.add(5,5))
print(calc.substract(5,2))
print(calc.multuply(5,1))
print(calc.division(1,12))
print(calc.division(1,0))

print("======================")

print("Задание 4:")
print(human1)
#В классе Human переопределен метод __str__
print("======================")
 

print("Задание 5:")
class Employee:
    def __init__(self) -> None:
        pass

    def get_paid():
        return 10000

class Manager(Employee):
    def __init__(self) -> None:
        super().__init__()
    
    def get_paid():
        return 35000

class Worker(Employee):
    def __init__(self) -> None:
        super().__init__()
    
    def get_paid():
        return 15000
    
emp = Manager
emp2 = Worker
print(emp.get_paid(),emp2.get_paid())