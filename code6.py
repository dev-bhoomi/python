#Python program to print even length words in a string
s = "This is a python language"
word=s.split()
for i in word:
    if len(i)%2==0:
        print(i,"", end="")