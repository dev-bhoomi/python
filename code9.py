#Remove All Duplicates from a Given String in Python
s = "geeksforgeeks"
x=set()
res=""
for i in s:
    if i not in x:
        x.add(i)
        res= res+i
print(res)