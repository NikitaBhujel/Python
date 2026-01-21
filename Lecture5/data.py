import json

'''
json.loads():JSON string loaded(converted) into python objects
json.dumps():python object converted into JSON string
'''

'''
json_str='{"name":"Nikita","isStudent":true}' #JSON data is stored in the form of python string
py_obj=json.loads(json_str)
print(type(json_str))
print(type(py_obj),py_obj)

'''

'''
py_obj={
    "name":"Anjali",
    "Age":None
}

json_str=json.dumps(py_obj)
print(type(json_str),json_str)
'''

'''
While dealing with files, use:
json.load
json.dump

'''
'''
with open("Lecture5/data.json","r") as f:
    py_obj=json.load(f)
    print(py_obj,type(py_obj))
'''


#python format dictionary
data={

    "name":"Anjali",
    "Age":None
}
with open("Lecture5/data.json","w") as f:
    json.dump(data,f,indent=4,sort_keys=True)
#single line data can be converted in different lines through indentation
#We can sort the data too