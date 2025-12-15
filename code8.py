#Count the Number of matching characters in a pair of string
s1 = "apple"
s2 = "grape"
res=set()
for i in s1:
    for j in s2:
        if i==j:
            res.add(i)
print(sorted(res))
print(len(res))