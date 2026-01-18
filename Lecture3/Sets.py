#Sets are collection of unique elements
#Set data types are immutable but set is MUTABLE

'''
s={1,2,3,3}
print(type(s))

#Sets are unordered

s.add(5)
print(s)

empty_set={ } #This gives empty dictionary
empty=set() #We are calling constructor function
print(type(empty))

'''
 #Methods in Set
s={1,2,3,4}
s.add(6)
print(s)

s.remove(1)
print(s)

#s.clear -> emptys the set elements
#s.clear()
#print(s)
s.pop() #removes a random value
print(s)

#s.union(set2) returns new union
#s.intersection(set2) returns new intersection

s2={2,5,9,7}
print(s.union(s2))
print(s.intersection(s2))

