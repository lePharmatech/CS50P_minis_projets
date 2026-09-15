import requests
import sys


try:
    x = float(sys.argv[1])
    r = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=a4044378d8c4dea904f0a37e3a4d0e2e5fc02bcd319ff2cec234b727376544d3")
    # print(x)
except IndexError:
        sys.exit("Missing command-line argument")
except ValueError:
        sys.exit("Command-line argument is not a number")
except requests.RequestException:
        sys.exit()
else:
    response = r.json()
    # print(response)
    amount = response['data']['priceUsd']
    amount = x * float(amount)
    print(f"${amount:,.4f}")
