#Maximum Frequency Character in String - Python
s = "hello world"
#x=s.split()
count={}
for i in s:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
max_count=max(count,key=count.get)
print(max_count)
print(count)
