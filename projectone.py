import math
class Person():
    def __init__(self, name, id, age):
        self.name = name
        self.id = id
        self.age = age











class Employee(Person):
    def __init__(self, salary):
        self.salary = salary


def main():
    size = int(input('Enter size for arr'))
    arr = []
    for i in range(size):
        type = input("Enter type of person(Studen , Employee,WorkingStudent):")