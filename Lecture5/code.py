''''
f=open("Lecture5/sample.txt","a") #file object is stored in 'f' variable

f.write("\nAppend mode")

'''
'''
data=f.readline()
print(data)
data=f.readline()
print(data)
'''

'''
data=f.read()
print(data)
print(type(data))
'''
#f.close()

#Write mode overwrites the complete text
#x:Creates new and open for writing

'''
f=open("Lecture5/sample2.txt","x")
f.write("Hi Nicks")
f.close()
'''


#binary mode, text mode, combined mode (rt,wt,rb,wb)
# +:opens disk file for uodate(r&W), + can be used with multiple modes(a+,r+,w+)
#a+:both append and read


