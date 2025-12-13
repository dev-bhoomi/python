snake_case = "python_language"
seperate= snake_case.split('_')
capitalized_words= [i.capitalize() for i in seperate]
pascal_case= ''.join(capitalized_words)
print(pascal_case)