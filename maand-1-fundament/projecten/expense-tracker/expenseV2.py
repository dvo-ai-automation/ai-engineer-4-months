import json

#FUNCTIES AANROEPEN
def main():
    aanvullen()
    totaal_bedrag = totaal_optellen()
    maand_bedrag = maand_optellen()
    print(f"Het totale bedrag is: €{totaal_bedrag}")
    print(f"Totaal bedrag voor deze maand: €{maand_bedrag}")

#JSON FILE OPENEN EN WEGSCHRIJVEN
def aanvullen():
    with open('expenses.json', 'r') as lezen:
        data = json.load(lezen)

    data.append({"bedrag": 50.00, "datum": "2026-09-17", "opmerking": "koffie"})

    with open('expenses.json', 'w') as schrijven:
        json.dump(data, schrijven, indent=2)
    return data

#TOTAAL OPTELLEN
def totaal_optellen():
    with open('expenses.json', 'r') as costs:
        uitgaven = json.load(costs)
    totaal_bedrag = sum(item["bedrag"] for item in uitgaven)
    return totaal_bedrag

#TOTAAL BEDRAG TONEN PER MAAND
def maand_optellen():
    with open('expenses.json', 'r') as month:
        maand = json.load(month)
    maand_bedrag = sum(item["bedrag"] for item in maand if item["datum"].startswith("2026-08"))
    return maand_bedrag

if __name__ == "__main__":
    main()