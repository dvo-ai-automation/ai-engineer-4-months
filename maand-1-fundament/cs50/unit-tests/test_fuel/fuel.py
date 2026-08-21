def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
        except (ZeroDivisionError, ValueError):
            continue
        break
    print(gauge(percentage))

def convert(fraction):
    parts = fraction.split("/")
    x = int(parts[0])
    y = int(parts[1])
    if x < 0:
        raise ValueError
    if y == 0:
        raise ZeroDivisionError
    if x > y:
        raise ValueError
    percentage = (round(x / y * 100))
    return percentage

def gauge(percentage):
    if percentage <= 1:
        return("E")
    elif percentage >= 99:
        return("F")
    else:
        return(f"{percentage}%")

if __name__ == "__main__":
    main()
