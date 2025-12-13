#Given a string, the task is to find how many times each word appears in it
text= "hello world hello everyone"
words= text.split()  
x=""
for i in words:
    if i != x:
        x=x.strip(i)
print(x)



#why we split??
#The split() method in Python is used to break a string into a list of words or substrings, using spaces
#"Python is fun" and splits it into the list ['Python', 'is', 'fun']