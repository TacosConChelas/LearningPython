from collections import deque

def is_palindrome(s: str) -> bool:
    s = s.lower().replace(" ", "")  # optional cleanup
    phrase_queue = deque(s)

    for ch in reversed(s):  # stack behavior
        if ch != phrase_queue.popleft():
            return False
    return True


def main():
    phrase = input("Enter a phrase: ").strip()
    print("It's a palindrome" if is_palindrome(phrase) else "It isn't a palindrome")

if __name__ == "__main__":
    main()
