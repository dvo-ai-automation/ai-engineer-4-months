s = input("Input: ")

vowels = "aeiouAEIOU"

for _ in s:
    if _ not in vowels:
        print(_, end="")
print()
