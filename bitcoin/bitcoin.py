import requests
import sys
import json

try:
    n = sys.argv[1]
    n = float(n)

    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    data_file = response.json()
    rate = data_file["bpi"]["USD"]["rate"]
    data_rate = float(rate.replace(",", ""))
    result = data_rate * n
    print(f"${result:,.4f}")

except ValueError:
    sys.exit("Command-line argument is not a number")
except IndexError:
    sys.exit("Missing command-line argument ")