'''
class Employee:
    start_time="10am"
    end_time="5pm"
class Teacher(Employee):  #Single Level Inheritance
    def __init__(self,subject):
        self.subject=subject
class Accountant(Teacher): #Multilevel inheritance
    def __init__(self,salary,subject):
        super().__init__(subject)
        self.salary=salary
a1=Accountant(20_0000,"Maths")
print(a1.subject,a1.salary,a1.start_time,a1.end_time)

'''

#Multiple Inheritance
class Teacher:
    def __init__(self,salary):
        self.salary=salary
class Student:
    def __init__(self,gpa):
        self.gpa=gpa
class TA(Teacher,Student):
    def __init__(self, salary,gpa,name):
        super().__init__(salary)  #Call constructor of first inherited class
        Student.__init__(self,gpa) #Use class name to call second constructor
        self.name=name
ta1=TA(10_000,4.0,"Uma")
print(ta1.salary,ta1.gpa,ta1.name)

