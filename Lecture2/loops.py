'''

count=1 #  counter/iterator
while count<=5:
    print("Hello Sunita")
    count+=1
print("After loop, count=",count)
'''
'''
i=1
while (i<=10):
 if (i % 6 == 0):
  break
 print(i)
 i+=1
print("Outside loop now")
'''

#continue keyword is used to skip current iteration and continue next iteration
'''
i=1
while(i<=10):
    if(i % 3==0):
        i+=1
        continue
    
    print(i)
    i+=1
print("Outside loop")
'''
#print all odd numbers without using continue
'''
i=1
while(i<=10):
    print(i)
    i+=2
'''
#using continue, print all odd numbers
'''
i=1
while(i<=10):
    if(i%2==0):
        i+=1
        continue
    print(i)
    i+=1

'''
'''
i=0
while(i<10):
    i+=1
    if(i%2==0):
        continue
    print(i)
'''