'''
name=input("Enter your full name:")
age=input("Enter your age:")
print("Hello",name, ", you are", age,"years old!")
'''

'''
a=float(input("enter num1:"))
b=float(input("enter num2:"))
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
'''

'''
#Ask the user to enter two integers and one float. Convert them all to floats and print their average.

num1=int(input("Enter first integer number:"))
num2=int(input("Enter second integer number:"))
num3=float(input("Enter third float number"))
a=float(num1)
b=float(num2)
avg=(a+b+num3)/3
print("The average of three numbers is:",avg)
'''

'''
#The user enters a string containing a number(e.g."45"). Convert it to integer, float and a string again. Print all three values with their types.

a=input("Enter number: ")
print(a,type(a))
b=int(a)
print(b,type(b))
c=float(b)
print(c,type(c))
d=str(c)
print(d,type(d))
'''

'''
#Evaluate and print the result of the following expression: x=10+3*2**2

x=10+3*2**2
print(x)
'''

'''
#Write a program to swap values of two numbers entered by the user.

a=input("Enter first number:")
b=input("Enter second number:")
print("a:",a)
print("b:",b)
x=a
a=b
b=x
print("a:",a)
print("b:",b)
'''

'''
#Ask the user for a temperature in Celsius(string input). Convert it to float,then calculate and print temperature in Fahrenheit

celsius_temp=input("Enter temperature in Celsius:")
celsius_temp=float(celsius_temp)
fahrenheit_temp=(celsius_temp *(9/5))+32
print("fahrenheit_temp:",fahrenheit_temp)
'''

'''
#Take the radius(r) as user input and print the area.

radius=float(input("Enter radius:"))
Area=3.14*radius**2
print("Area:",Area)
'''

'''
#Ask the user for : Principal(P),Rate(R),Time(T).Convert all to float and compute simple interest:
P=input("Enter principal:")
R=input("Enter rate:")
T=input("Enter Time:")

SI=(float(P)*float(T)*float(R))/100
print("SI:",SI)
'''

'''

#Take a decimal number as input (like 45.78) and output its: integer part-45 and fractional part-78

num=float(input("Input decimal number:"))
integer_Part=print(int(num))

'''

'''
num = input("Enter a decimal number: ")
integer_part, fractional_part = num.split(".")
print("Integer part =", integer_part)
print("Fractional part =", fractional_part)

'''