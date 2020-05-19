from peewee import *

db = MySQLDatabase('py-test')


def test1():
    pass


class people:
    def printPeople(self):
        print("hello people")


def displayCount():
    print("Total Employee")


class Employee(people):
    '所有员工的基类'
    empCount = 0

    def __init__(self, name='', salary=''):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

if __name__ == '__main__':
    e1 = Employee()
    e2 = Employee()
    print(id(e1))
    print(id(e2))