#Key:Value pairs where keys are always unique
#Dictionaries are unordered

info={
    "name":"Nikita",
    "cgpa":4,
    "subjects":["Science","Maths"],
    3.14:"PI"
}

'''
print(type(info))
print(info)
print(info[3.14])
'''
info["cgpa"]=3.96
print(info)