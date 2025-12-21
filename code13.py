#Find words which are greater than given length k
str = "hello geeks for geeks is computer science portal" 
x=str.split()
k=5
for i in x:
    if len(i)>k:
        print(i)
    
