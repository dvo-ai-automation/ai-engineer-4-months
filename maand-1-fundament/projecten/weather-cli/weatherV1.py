import requests

r = requests.get(
    "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m&models=knmi_seamless&forecast_days=3"
)

data = r.json()
tijd = data["hourly"]["time"][0]
temp = data["hourly"]["temperature_2m"][0]
celsius = data["hourly_units"]["temperature_2m"]

print(f"De temperatuur op {tijd} wordt {temp}{celsius}")