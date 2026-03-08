import requests
import sys

def main():
    for word in sys.stdin:
        res = requests.get(url=f"https://jsonplaceholder.typicode.com/{word}")
        if res.status_code == 404:
            main()
        else:
            print(f'word: {word}\nStatus Code: {res.status_code}')
            print(res.json())

if __name__ == '__main__':
    main()