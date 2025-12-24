#Python - Replace all Occurrences of a Substring in a String
input= "python java python html python"
s=input.split()
replace ="python", "c++"
for i in s:
    new=input.replace("python","c++")
print(new)
