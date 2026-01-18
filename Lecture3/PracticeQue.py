info=[("Alice","Maths"),
      ("Bob","Science"),
      ("Alice","Science"),
      ("Charlie","Maths"),
      ("Bob","Maths"),
      ("Alice","English"),
      ("Charlie","English"),
      
      ]
'''
unique_courses=set()
for tup in info:
    unique_courses.add(tup[1]) #Course values
print(unique_courses)
'''

'''
for tup in info:
    print(tup)
'''

'''
for name,course in info:
   # print(name,course)
    if(course=="English"):
      print(name)
'''

'''
for tup in info:
    if(tup[1]=="English"):
        print(tup[0])

'''

dictionary={}
for name,course in info:
    if(dictionary.get(name)==None):
        dictionary.update({name:set()})
        dictionary[name].add(course)
    else:
        dictionary[name].add(course)
print(dictionary)