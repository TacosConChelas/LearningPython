import requests

def main():
    try:
        resultado = requests.get("Https://api.artic.edu/api/v1/artworks/search")
        for art in resultado.json()["data"]:
            print(f"* {art["title"]}")
    except requests.HTTPError:
        print("Couldn't complete request...")
        return
        
if __name__ == "__main__":
    main()