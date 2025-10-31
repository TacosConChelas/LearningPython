def count_up_to(n):
    for i in range(1, n + 1):
        yield i
def main():
    gen = list(count_up_to(5))
    print(gen)
    # for num in gen:
    #    print(num)


if __name__ == "__main__":
    main()

