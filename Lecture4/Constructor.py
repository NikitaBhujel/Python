#Constructors are the functions which create objects

#_init_Method is a constructor, to initialize objects(assign initial properties)
#Init method gets called automatically

class Student:
    def __init__(self,name,cgpa):
        self.name=name
        self.cgpa=cgpa
    def get_cgpa(self):
        return self.cgpa
        #print("Constructor was called")
          #Self is compulsory parameter, it is storing current instance of the class
stu1=Student("Neha",4.0)
stu2=Student("Nikita",4.0)
print(stu1.name,stu1.cgpa)
print(stu2.name,stu2.cgpa)

print(stu1.get_cgpa())
print(stu2.get_cgpa())