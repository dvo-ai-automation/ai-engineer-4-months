import json
from datetime import datetime

while True:
    try:
        argument = input("Input (bedrag, yyyy-mm-dd, opmerking): ")
        delen = argument.split(",")
        for deel in range(len(delen)):
            delen[deel] = delen[deel].strip()
        if len(delen) < 3:
            print("Te weinig data")
            continue
        elif len(delen) > 3:
            print("Te veel data")
            continue
        try:
            bedrag = float(delen[0])
        except ValueError:
            print("bedraginvoer was onjuist")
            continue
        try:
            tijd = datetime.strptime(delen[1], "%Y-%m-%d")
            tijd = tijd.strftime("%Y-%m-%d")
        except ValueError:
            print("tijdinvoer was onjuist")
            continue
        opmerking = delen[2]
        print(f"Jouw uitgave is bevestigd met: €{bedrag:.2f}, {tijd} en de opmerking: {opmerking}")
    except EOFError:
        break

    d = {"bedrag": 12.50, "datum": "2026-08-17", "opmerking": "koffie"}

    with open('expenses.json', 'r', encoding='utf-8') as bestand:
        data = json.load(bestand)

    print(data)