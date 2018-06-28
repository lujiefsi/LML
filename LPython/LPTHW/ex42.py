'''
Created on Jun 28, 2018

@author: lujie
'''
from LPython.LPTHW.ex5 import name
class Animal(object):
    pass
class Dog(Animal):
    def __init__(self,name):
        self.name = name

class Fish:
    def __init__(self,name):
        self.name = name
class Person:
    def __init__(self,name):
        self.name = name
        self.pet = None
class Employee(Person):
    def __init__(self,name,salary):
        super(Employee,name).__init__(name)
        self.salary = salary
        
revoey = Dog("revey")
paopao=Fish("paopap")
lujiefsi = Employee("lujiefsi")
lujiefsi.pet = paopao

    