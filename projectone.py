import math

class Person():
    def __init__(self, name, id, age):
        self.name = name
        self.id = id
        self.age = age







class Employee(Person):
    def __init__(self, salary):
        self.salary = salary


class Student(Person):
    def _init_(self, avrg, ins):
        self.average = avrg
        self.institute = ins



def main():
    size = int(input('Enter size for arr'))
    arr = []
    for i in range(size):
        type = input("Enter type of person(Student , Employee, WorkingStudent):")



