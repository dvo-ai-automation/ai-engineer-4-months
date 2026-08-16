import inflect
p = inflect.engine()

namen = []
while True:
    try:
        names = input("Name: ")
        namen.append(names)
    except EOFError:
        break

lijst = p.join(namen)
print()
print(f"Adieu, adieu, to {lijst}")
