import sys

try:
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    else:
        if sys.argv[1].endswith(".py"):
            with open(sys.argv[1]) as file:
                count = 0
                for line in file:
                    if not line.strip() == "":
                        if not line.strip().startswith("#"):
                            count = count + 1
                        else:
                            continue
                    else:
                        continue
                print(count)
        else:
            sys.exit("Not a Python file")
except FileNotFoundError:
    sys.exit("File does not exist")
