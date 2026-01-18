info={
    'age':20,
    'address':'Sindhuli'
}
print(info.keys())
print(list(info.keys()))
#dkeys() returns all keys

print(info)
print(info.values()) #d.values returns all values
print(info.items())  #d.items () returns key value pairs

#d.get(key) returns val acc. to key
# #shows error and lines below it are not executed
print(info.get("name"))

#d.update (items) is used to update the dictionary.
info.update({

    "Name":"Nikita"
})
print(info)