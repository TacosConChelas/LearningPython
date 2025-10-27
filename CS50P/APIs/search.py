from museum.api3 import get_artist

def main():
    artwork = input("Artwork: ")
    artworks = get_artist(query=artwork, limit=3)
    for artwork in artworks:
        print(f"* {artwork}")

main()