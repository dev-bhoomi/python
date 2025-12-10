#the task is to reverse the words in it without changing the words themselves
s = "Python is fun"
words=s.split()  ## words = ['Python', 'is', 'fun']
res=" "
for i in range(len(words)-1,-1,-1):
    res= res+ words[i]+ " "

res=res.strip()
print(res)

#In for i in range(len(words)-1, -1, -1), the three parts mean:
#Start: The loop starts at len(words)-1, which is the index of the last word in the list.
#Stop: The loop stops before -1, so it goes down to index 0 (the first word).
#Step: The loop decreases by 1 each time (third argument is -1).
#So, the loop goes from the last index to the first, one by one. For example, if words = ['Python', 'is', 'fun'], the loop runs for i = 2, 1, 0