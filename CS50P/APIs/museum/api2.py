import requests


def main():
    artwork = input("Artwork: ")
    artworks = get_artworks(query=artwork, limit=3)
    for artwork in artworks:
        print(f"* {artwork}")
    
def get_artworks(query, limit):
    try:
        response = requests.get(
            "Https://api.artic.edu/api/v1/artworks/search",
            {"q": query, "size" : limit}
        )
        response.raise_for_status()
    except requests.HTTPError:
        return []
    
    content = response.json()
    return [artwork["title"] for artwork in content["data"]]

if __name__ == "__main__":
    main()