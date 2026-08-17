import json

with open('expenses.json', 'r') as lezen:
    data = json.load(lezen)

data.append({"bedrag": 50.00, "datum": "2026-09-17", "opmerking": "koffie"})

with open('expenses.json', 'w') as schrijven:
   json.dump(data, schrijven, indent=2)