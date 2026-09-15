import requests
import json

def main():
    try:
        response = requests.get("https://api.artic.edu/api/v1/artworks/search")

    except requests.HTTPError:
        print("l'appel n'a pas été effective")
    else:
        o = response.json()
        print(json.dumps(o, indent = 2))
        for i in o['title']:
            print(i)

main()
