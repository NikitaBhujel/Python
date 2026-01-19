# Q1 Ask the user for a string and check whether it is a palindromeornot.

'''
s = 'Nikita'
i = len(s)
rev = ""
while i > 0:
    ch = s[i - 1]
    i = i - 1
    rev = rev+ch
print(rev)
if s == rev:
    print(f"{s} is a palindrome")
else:
    print(f"{s} is not a palindrome")

'''

'''
s = input("Enter a string: ")
rev = ""
for ch in s:
    rev = ch+rev
if s == rev:
    print("Palindrome")
else:
    print("Not a Palindrome")
'''


#Q2 Given a list of integers compute the average of all numbers in the list.

'''
Num=[1,2,3,4,5]
sum=0
for n in Num:
    sum=sum+n
print(sum)
Average=sum/len(Num)
print(Average)
'''


#Q3 Input two lists of integers from the user. Merge them into one list and sort the result

'''
list1 = list(map(int, input("Enter elements of first list: ").split()))
list2 = list(map(int, input("Enter elements of second list: ").split()))

# Merge the lists
merged = list1 + list2
print("Merged list:", merged)

# we can sort list directly using merged.sort()

for i in range(len(merged)):
    for j in range(i + 1, len(merged)):
        if merged[i] > merged[j]:
            merged[i], merged[j] = merged[j], merged[i]
print("Sorted list", merged)
'''

#Q4 Given a tuple of integers, create: A tuple of all even numbers and A tuple of all odd numbers
'''
Tup=(1,2,4,6,3,9)
Odd=()
Even=()
for n in Tup:
    if(n%2==0):
        Tup1=Tup1+n
    else:
        seen.add(item)
print("Elements that appear more than once:", duplicates)
'''

# Q10
s = input("Enter a string: ")
# Find unique characters using set
unique_chars = set(s)
print("Unique characters:", unique_chars)
# Print the count of unique characters
print("Number of unique characters:", len(unique_chars))
