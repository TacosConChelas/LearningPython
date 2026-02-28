import requests
import sys

def main():
    for word in sys.stdin:
        res = requests.get(url=f"https://jsonplaceholder.typicode.com/{word}")
        print(res)
        print(res.json())

if __name__ == '__main__':
    main()