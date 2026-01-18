'''
block of stataments that perform specific task
definition ma logic lekhxam and function call (invoke) garne
functions are resuable components in code
'''
'''
we use def keyword to define function
def function():
    ......
    ......
'''

'''
def hi():
    print("Hello Shraddha")
hi() #function call

'''

'''
def addition(a,b):
    add=a+b
    return add

#function call
a=addition(3,9)
print(a)
'''

#function to calculate average of 3 numbers

'''
def average(a,b,c):
    avg=(a+b+c)/3
    return avg
a=int(input("Enter number1:"))
b=int(input("Enter number2:"))
c=int(input("Enter number3:"))
d=average(a,b,c)
print("The average is:",d)

or

def calc_ave(a,b,c):
    sum=a+b+c
    return sum/3
print(calc_ave(2,2,2))
'''

#We can use default values for function as well
#We are implementing logic where by default when we pass 5, then 1 is added with 5, like sum(5,1)
#Generally non-default parameters are written at first and non-default is written at last

'''
def summ(a,b=1):
    add=a+b
    return add
print(summ(5))
'''

