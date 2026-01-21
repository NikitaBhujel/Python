'''
data=True
count=0
with open("Lecture5/sample.txt") as f:
    while data:
        count+=1
        data=f.readline()
        print(data)
        if("Python" in data):
            print("Word found")
            print(f"Line number:{count}")
        
'''

data=True
line=1
word="Python"
with open("Lecture5/sample.txt") as f:
    while data:
        data=f.readline()
        if(word in data):
            print(f"{word} found at line {line}")
            break
        line+=1

