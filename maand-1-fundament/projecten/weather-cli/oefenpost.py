import requests

r = requests.post(
    "https://postman-echo.com/post", 
    json={"naam": "Dylan"}
              )

data = r.json()

print(data["json"]["naam"])