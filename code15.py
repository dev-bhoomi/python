#Replace Multiple Words with K - Python
text = "apple orange banana"
words_to_replace = "apple", "banana"
k="K"
for i in words_to_replace:
    text=text.replace(i,k)
print(text)
