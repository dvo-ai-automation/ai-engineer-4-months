while True:
    try:
        fraction = input("Fraction: ")
        fraction = fraction.split("/")

        x = int(fraction[0])
        y = int(fraction[1])
        percentage = (round(x / y * 100))
    except (ValueError, ZeroDivisionError):
        continue
    if x > y:
        continue
    if x < 0:
        continue
    break
if percentage <= 1:
    print("E")
elif percentage >= 99:
    print("F")
else:
    print(f"{percentage}%")
