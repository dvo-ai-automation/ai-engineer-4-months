def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not s.isalnum():
        return False
    if not (2 <= len(s) <= 6):
        return False
    if not s[0:2].isalpha():
        return False
    seen_digit = False
    for item in s:
        if item.isdigit():
            if seen_digit == False:
                 if item == "0":
                    return False
            seen_digit = True
        elif seen_digit == True:
            return False

    return True

main()
