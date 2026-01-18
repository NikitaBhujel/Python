#dynamic string:different variables and values
#format() function:came with version3, we use placeholder and placement values, placeholder is curly braces
''''
a=5
b=10
sum=a+b

#This is normal formatting.

print("Sum is {}".format(sum))
print("Language is {}".format("python"))
print("Sum is {}".format("python")) #{} is placeholder for sum and python

print("sum of {} & {} is {}".format(a,b,sum))

#Index based formatting
print("sum of {1} & {0} is {2}".format(a,b,sum))


 #Value Based Formatting
print("{a} Values of vars {a} & {b}".format(a=5,b=10))
'''

#F-strings
#Literal string interpolation

# f"{ }":variable and expression are written inside curly braces
a=5
b=10
print(f"sum of {a} and {b} is {a+b}")
    

