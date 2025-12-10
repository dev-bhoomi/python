s=input("enter a string ")
res= ' '.join(s.split()[::-1])
print(res)

#Why we use split()?
#splitting allows us to reverse the order of words. When you split a string, each word becomes a separate item in a list. This makes it easy to reverse the list (to change word order) 