#Find all Duplicate Characters in String in Python
x= "GeeksforGeeks"
count={}
res=[]
for i in x:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
for y in count:
    if count[y]>1:
        res.append(y)
        
print(res)
