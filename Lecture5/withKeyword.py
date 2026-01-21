with open("Lecture5/sample.txt","r") as f:
    data=f.read()
    print(len(data))

#Use os module to delete file

import os
os.remove("Lecture5/sample2.txt")