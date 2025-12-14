#Python Program to Accept the Strings Which Contains all Vowels
x="geeksforgeeks"
y=set('aeiou')
z=set()
for i in x.lower():
    if i in y:
        z.add(i)
if y==z:
    print("String contains all vowels")
else:
    print("String does not contain all vowels")