import os
import requests
import sys

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("COINCAP_API_KEY")

if len(sys.argv) == 2:
    if not API_KEY:
        sys.exit("Set COINCAP_API_KEY first (see README.md)")

    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Need a number 'n'")

    try:
        r = requests.get(
            "https://rest.coincap.io/v3/assets/bitcoin",
            headers={"Authorization": f"Bearer {API_KEY}"},
            timeout=10,
        )
        json = r.json()
        btc = float(json["data"]["priceUsd"]) * n
        print(f"${btc:,.4f}")
    except requests.RequestException:
        sys.exit("couldn't fetch coincap.io")

else:
    sys.exit("Need a number 'n'")
