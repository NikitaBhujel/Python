#Q1
'''
salary=int(input("Enter salary:"))
if salary<30000:
    print("The tax rate for", salary, "is 5%.")
elif 30000<salary<70000:
    print("The tax rate for", salary, "is 15%")
else:
    print("The tax rate for",salary ,"is 25%")
'''


# Q2 Write a function that takes two integers and and prints all even
# numbers between them (inclusive).

num=int(input("Enter number1:"))
num1=int(input("Enter number2:"))
for i in range(num,num1+1):
    if(i%2==0):
        print(i)



'''
#Q3
n=int(input("Enter number:"))
digit1=n%10
print("Digit1:",digit1)
a=int(n/10)
print(a,type(a))
digit2=a%10
print("Digit2:",digit2)
b=int(a/10)
digit3=b%10
print("Digit3:",digit3)
'''

'''
#Q4 Write a function to return the count the number of digits in a number, n .

def count_digits(n):
    if n == 0:
        return 1
    count = 0
    n = abs(n)   # handle negative numbers
    while n > 0:
        n //= 10
        count += 1
    return count
print(count_digits(122))
'''
'''
#Q5 Write a function to return the sum of digits of a number, n .

def sum_of_digits(n):
    n=abs(n)
    sum=0
    while n>0:
        digit=n%10
        sum+=digit
        n//=10
    return sum
print(sum_of_digits(23))
'''

#Q6 Write a program to print all numbers from 1 to 100 that are divisible by both 3 and 5
'''
for n in range(1,100+1):
    if (n%3==0 and n%5==0):
        print(n)
'''

#Q7 Design a program to continuously input a number from user & print if it is positive or negative until the user enters “Quit”.
'''
while True:
    user_input = input("Enter a number (or type Quit to exit): ")
    if user_input.lower() == "quit":
        print("Program terminated.")
        break
    num = float(user_input)
    if num > 0:
        print("Positive number")
    elif num < 0:
        print("Negative number")
    else:
        print("Zero")
'''

#Q8 simple calculator
'''
def calculator(a,b,operation):
    if operation=='+':
        print("Sum:",a+b)
    elif operation=='-':
        print("Subtraction:",a-b)
    elif operation=='*':
        print("Multiplication:",a*b)
    elif operation=='/':
        if b!=0:
         print("Division",a/b)
        else:
            print("Divide by zero")
    else:
        print("Invalid choice")
calculator(4,2,'*')
'''

#Q9
'''
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

print(is_prime(3))
print(is_prime(1))
print(is_prime(8))
'''

'''
#Q10
num=int(input("Guess your number:"))
if num>100:
    print("The guesss is above the number.")
elif num<100:
    print("The guess is too low.")
else:
    print("Correct!")
'''