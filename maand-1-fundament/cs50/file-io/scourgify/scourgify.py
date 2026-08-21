import csv
import sys

try:
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1].endswith(".csv"):
            with open(sys.argv[1], "r") as before, open(sys.argv[2], "w") as after:
                reader = csv.DictReader(before)
                writer = csv.DictWriter(after, ["first", "last", "house"])
                writer.writeheader()
                for row in reader:
                    naam_delen = row["name"].split(",")
                    first = naam_delen[1].strip()
                    last = naam_delen[0].strip()
                    writer.writerow(
                        {
                            "first": first,
                            "last": last,
                            "house": row["house"],
                        }
                    )
        else:
            sys.exit("Not a CSV file")
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")

