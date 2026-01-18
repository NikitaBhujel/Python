#For lambda functions, we write lambda and parameters are separated by comma and we use mathematical expression usually
#We can only have a single expression
#We dont use lamba expression for large and complex expressions, we use normal functions

'''
sum=lambda a,b,c:a+b+c
print(sum(1,2,3))
'''

#High order functions have functions as parameters or return function as value
#WAF to print factorial of'n'
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
print(factorial(5))

    