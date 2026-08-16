import random


def main():
    level = get_level()
    score = 0
    for _ in range(10):
        poging = 0
        x = generate_integer(level)
        y = generate_integer(level)
        while True:
            som = input(f"{x} + {y} = ")
            try:
                if int(som) == x + y:
                    score = score + 1
                    break
                else:
                    print("EEE")
                    poging = poging + 1
                    if poging == 3:
                        print(f"{x} + {y} = {x + y}")
                        break
            except ValueError:
                print("EEE")
                poging = poging + 1
                if poging == 3:
                    print(f"{x} + {y} = {x + y}")
                    break

    print(f"Score: {score}")

def get_level():
    while True:
        try:
            n = input("Level: ")
            if int(n) in [1, 2, 3]:
                return int(n)
            else:
                continue
        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        return x
    elif level ==2:
        x = random.randint(10, 99)
        return x
    elif level == 3:
        x = random.randint(100, 999)
        return x
    else:
        raise ValueError


if __name__ == "__main__":
    main()
