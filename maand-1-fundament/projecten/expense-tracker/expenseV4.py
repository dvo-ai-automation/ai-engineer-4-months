import json
from datetime import datetime

# Interactieve loop beheren met gebruiker
def main():
    print("Welkom bij de expense tracker. Typ Ctrl+D om te stoppen.\n")
    while True:
        try:
            argument = input("Input (bedrag, yyyy-mm-dd, opmerking): ")
            uitgave = valideer_input(argument)

            if uitgave == False:
                continue # Input was incorrect, vraag opnieuw

            # Bevestiging tonen
            print(f"Jouw uitgave is opgeslagen")

            # Opslaan in JSON
            aanvullen(uitgave)

        # User sluit af, programma toont totale kosten
        except EOFError:
            print("\n")
            print("Programma is succesvol afgesloten\n")
            totaal_bedrag = totaal_optellen()
            maand_bedrag = maand_optellen()
            print(f"Totale uitgaven vandaag: €{totaal_bedrag:.2f}")
            print(f"Totale uitgaven deze maand is: €{maand_bedrag:.2f}")
            break

def valideer_input(argument):
        delen = argument.split(",")
        for deel in range(len(delen)):
            delen[deel] = delen[deel].strip()

        try:
            bedrag = float(delen[0])
        except ValueError:
            print("Bedraginvoer was onjuist")
            return False

        if len(delen) < 3:
            print("Te weinig data")
            return False
        
        if len(delen) > 3:
            print("Te veel data")
            return False
        
        try:
            tijd_obj = datetime.strptime(delen[1], "%Y-%m-%d")
            tijd = tijd_obj.strftime("%Y-%m-%d")
        except ValueError:
            print("Tijdinvoer was onjuist")
            return False
        
        opmerking = delen[2]
        return {"bedrag": bedrag, "datum": tijd, "opmerking": opmerking}

#JSON FILE OPENEN EN WEGSCHRIJVEN
def aanvullen(uitgave):
    with open('expenses.json', 'r') as lezen:
        data = json.load(lezen)

    data.append(uitgave)

    with open('expenses.json', 'w') as schrijven:
        json.dump(data, schrijven, indent=2)
    return data

#TOTAAL OPTELLEN VAN VANDAAG
def totaal_optellen():
    vandaag = datetime.now().strftime("%d")
    with open('expenses.json', 'r') as day:
        dag = json.load(day)
    totaal_bedrag = sum(item["bedrag"] for item in dag if item["datum"].endswith(f"{vandaag}"))
    return totaal_bedrag

#TOTAAL BEDRAG TONEN PER MAAND
def maand_optellen():
    huidige_maand = datetime.now().strftime("%Y-%m")
    with open('expenses.json', 'r') as month:
        maand = json.load(month)
    maand_bedrag = sum(item["bedrag"] for item in maand if item["datum"].startswith(f"{huidige_maand}"))
    return maand_bedrag

if __name__ == "__main__":
    main()
