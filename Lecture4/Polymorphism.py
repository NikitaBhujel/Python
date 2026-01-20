#Many forms, multiple functions with same name
'''
Operator overloading:
 '+' operator is used to perform addition and polymorphism
In case of object oriented programming:
1. Function overriding :Redefining parent class functions in child class
2.Duck Typing
'''

class Employee:
    def get_designation(self):
        print("Designation:Employee")
class Teacher(Employee):
    def get_designation(self):
        print("Designation:Teacher")
t1=Teacher()
t1.get_designation()