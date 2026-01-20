
class Teacher():
    def get_designation(self):
        print("Designation:Teacher")

class Accountant():
    def get_designation(self):
        print("Designation:Accountant")

t1=Teacher()
t1.get_designation()

t2=Accountant()
t2.get_designation()

'''
If it walks like a duck and quacks like a duck : It must be a duck
If an object has the methods or behavior you need, Python will use it—no matter its class or type.
'''