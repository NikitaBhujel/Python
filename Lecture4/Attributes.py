#class and instance -> class attributes belong to class and instance attributes belong to object
#Instance attributes can be different whereas class attributes are common
class student:
    college_name="Pk"
    PI=3.1
    def __init__(Self,name,gpa):
        Self.name=name
        Self.gpa=gpa
        Self.PI=3.14
stu1=student("Sushant",4.0)
print(stu1.name) #To access instance attributes, we need object
print(stu1.college_name)
print(student.college_name)
print(stu1.PI)  #Instance value is printed
print(student.PI) #With class bname it is called so PI value of class attribute is printed
#We can access class attributes through class name or object name
#If class and instance attributes are same then instance attributes have greater priority so it is printed
