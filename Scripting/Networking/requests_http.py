import requests
import sys

def main():
    res = requests.get(url="https://jsonplaceholder.typicode.com/posts/1")
    print(res)
    print(res.json())

if __name__ == '__main__':
    main()