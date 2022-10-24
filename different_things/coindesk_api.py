'''
Display the bitcoin price using information from the api CoinDesk.
Check: https://github.com/public-apis/public-apis
'''

import json
import requests

if __name__ == "__main__":

    code: str = input("Enter the currency code (EUR, GBP, USD, PLN): ")
    response = requests.get(f"https://api.coindesk.com/v1/bpi/currentprice/{code}.json")

    if response.status_code != requests.codes.ok:
        print("Something has gone wrong!")
    else:
        print(json.dumps(response.json(), indent=4))
