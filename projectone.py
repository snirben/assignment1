import math

class Person:
    def __init__(self, name, i_d, age):
        self.name = name
        self.i_d = i_d
        self.age = age

class Student(Person):
    def __init__(self, name, i_d, age, average, institute):
        Person.__init__(self, name, i_d, age)
        self.average = average
        self.institute = institute

    def funcprint(self):
        print("STUDENT:")
        print("Name:",self.name)
        print("ID:",self.i_d)
        print("Age",self.age)
        print("Average:",self.average)
        print("institute:",self.institute)


class Employee(Person):
    def __init__(self, salary):
        self.salary = salary

    def funcprint(self):
        print("EMPLOYEE:")
        print("Name:", self.name)
        print("ID:", self.i_d)
        print("Age", self.age)
        print("Salary:", self.salary)


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

def printall(arr):
    for i in range(0, len(arr)):
        arr[i].funcprint()



def start():
    size = int(input("Enter size for arr:"))
    arr = []
    for i in range(0, size):
        type = input("Enter type of person(Student , Employee, Workingstudent):")
        while type not in ('Student', 'Employee', 'Workingstudent'):
            print("This type is not exist!!\n Try again ")
            type = input("Enter type of person(Student , Employee, Workingstudent):")
        if type == "Student":
                name = input("Enter name:")
                i_d = input("Enter ID:")
                age = input("Enter age:")
                average = input("Enter avareage:")
                institute = input("Enter institute:")
                s = Student(name, i_d, age, average, institute)
                arr.append(s)
        if type == "Employee":
                name = input("Enter name:")
                i_d = input("Enter ID:")
                age = input("Enter age:")
                salary = input("Enter salary:")
                e = Employee(name, i_d, age, salary)
                arr.append(e)
        if type == "Workingstudent":
                name = input("Enter name:")
                i_d = input("Enter ID:")
                age = input("Enter age:")
                average = input("Enter avareage:")
                institute = input("Enter intitute:")
                salary = input("Enter salary:")
                same_institute = input("Are the Student from the same institute?:")
                w = WorkingStudent(name, i_d, age, average, institute, salary, same_institute)
                arr.append(w)
    printall(arr)

start()




