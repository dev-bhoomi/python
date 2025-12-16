#Least Frequent Character in String
s = "GeeksforGeeks"
count={}
for i in s:
    if i in count:
        count[i]+=1

    else:
        count[i]=1
least_char = min(count,key=count.get)
print(least_char)
print(count)
