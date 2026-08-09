month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ")
        parts = date.split()
        if not parts[1].endswith(","):
            raise ValueError("Geen komma gevonden")
        else:
            parts[1] = parts[1].strip(",")
            parts[1] = int(parts[1])
            parts[2] = int(parts[2])
            monthnmr = (month.index(parts[0])) + 1
    except(ValueError, IndexError):
        try:
            parts = date.split("/")
            monthnmr = int(parts[0])
            parts[1] = int(parts[1])
            parts[2] = int(parts[2])
        except(ValueError, IndexError):
            continue
    if monthnmr < 13 and parts[1] < 32:
        break
    else:
        continue

print(f"{parts[2]}-{monthnmr:02}-{parts[1]:02}")
