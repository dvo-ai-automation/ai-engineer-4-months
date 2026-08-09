d = {

}

while True:
    try:
        item = input()
        item = item.upper()
        if item in d:
            d[item] = d[item] + 1

        else:
            d[item] = 1
    except EOFError:
        break

for item in sorted(d):
    print(f"{d[item]} {item}")

