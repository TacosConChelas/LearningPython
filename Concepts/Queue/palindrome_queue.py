"""
5 ----
Check if a string is a palindrome using queue + stack
Use both data structures to compare characters.
"""
from collections import deque

def main():
    phrase = list(input("Enter the phrase: ").strip())
    # print(phrase)
    if is_palindrome(phrase):
        print("It's a palindrome")
    else:
        
        print("It isn't a palindrome")
        
def is_palindrome(phrase : list) -> bool:
    phrase_queue = deque(phrase)
    for item in phrase[::-1]:
        if item != phrase_queue.popleft():
            return False
    return True

if __name__ == "__main__":
    main()