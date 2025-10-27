"""
4) Given a list of numbers, return the sum of all even elements.
"""
def main():
    numbers_list = [1, 3, 4, 4, 6, 7, 8, 8, 9, 8]
    print(sum(num for num in numbers_list if num % 2 == 0))    
if __name__ == "__main__":
    main()