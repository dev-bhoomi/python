#Program to check if a string contains any special character
s = "hello@world"
special_char="!@#$%^&*()<>,./:;'~"
for i in s:
    if i in special_char:
        print("yes",i)
        break
else:
    print("no")