"""
1) ----- Countdown generator
Write a generator function countdown(n) that yields integers from n down to 1. 
Converting the generator to a list (list(countdown(3))) should produce [3, 2, 1].
"""
def main():
    print(list(countdown(4)))
def countdown(n):
    for i in range(n, 0, -1):
        yield i
if __name__ == "__main__":
    main()