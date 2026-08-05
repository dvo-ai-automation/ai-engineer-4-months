s = input("Camel case: ")
result = ""
for letter in s:
    if letter.isupper():
        result = result + "_" + letter.lower()
    else:
        result = result + letter
print(result)
