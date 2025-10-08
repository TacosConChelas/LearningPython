SHOWS = [
    " avathar: thje last airbender",
    "ben 10",
    " arthur",
    "Spongebob Squarepants",
    "Phineas and Ferb",
    "Kim possible",
    " Jimmy Neutron",
    "The Proud family"
]

def main():
    cleaned_dhows = []

    for show in SHOWS:
        cleaned_dhows.append(show.title().strip())

    print('\n'.join(cleaned_dhows))

main()