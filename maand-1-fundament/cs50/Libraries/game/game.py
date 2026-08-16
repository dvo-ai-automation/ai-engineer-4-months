import random

while True:
    try:
        n = int(input("Level: "))
    except ValueError:
        pass
    else:
        if n > 0:
            break

r = random.randrange(1, n + 1)

while True:
    try:
        g = int(input("Guess: "))
    except ValueError:
        pass
    else:
        if g > 0:
            if g < r:
                print("Too small!")
                continue
            elif g > r:
                print("Too large!")
                continue
            else:
                print("Just right!")
                break
