from collections import deque

def is_palindrome(s: str) -> bool:
    s = ''.join(ch.lower() for ch in s if ch.isalnum())  # keep only letters/numbers
    dq = deque(s)

    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True


def main():
    phrase = input("Enter a phrase: ").strip()
    print("It's a palindrome" if is_palindrome(phrase) else "It isn't a palindrome")

if __name__ == "__main__":
    main()
