import requests


def main():
    artwork = input("Artist: ")
    artworks = get_artist(query=artwork, limit=3)
    for artwork in artworks:
        print(f"* {artwork}")
    
def get_artist(query, limit):
    try:
        response = requests.get(
            "Https://api.artic.edu/api/v1/agents/search",
            {"q": query, "size" : limit}
        )
        response.raise_for_status()
    except requests.HTTPError:
        return []
    
    content = response.json()
    return [artist["title"] for artist in content["data"]]

if __name__ == "__main__":
    main()