import math

class Person():
    def __init__(self, name, id, age):
        self.name = name
        self.id = id
        self.age = age

class Student(Person):
    def __init__(self, name, i_d, age, average, institute):
        Person.__init__(self, name, i_d, age)
        self.average = average
        self.institute = institute



class Employee(Person):
    def __init__(self, salary):
        self.salary = salary



class WorkingStudent(Employee, Student):
    def __init__(self, name, i_d, age, average, institute, salary, same_institute):
        Employee.__init__(self, name, i_d, age, salary)
        Student.__init__(self, name, i_d, age, average, institute)
        self.same_institute = same_institute

    def funcprint(self):
        print("WORKINSTUDENT:")
        print("Name:", self.name)
        print("ID:", self.i_d)
        print("Age", self.age)
        print("Average:", self.average)
        print("institute:", self.institute)
        print("Salary:", self.salary)
        print("Are the Student from the same institute:",self.same_institute)



def main():
    size = int(input('Enter size for arr'))
    arr = []
    for i in range(size):
        type = input("Enter type of person(Student , Employee, WorkingStudent):")



