'''
squares=[]
for i in range(5):
    squares.append(i*i)
print(squares)

'''

# [output for item in iterable if condition]
#condition is not compulsory, it is used if required

sq=[i*i for i in range(5)]
print(sq)

sq=[i*i for i in range(5) if i%2!=0]
print(sq)


#if else can be used as well after output part
nums=[-1,-2,0,5,4,-1]
nums=[0 if val<0 else val for val in nums]
print(nums)

words=["hello","python","Nikita"]
words=[val.upper() for val in words]
print(words)


