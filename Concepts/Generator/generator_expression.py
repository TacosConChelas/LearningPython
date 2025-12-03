"""
3) ------ Generator expression for a sum
Use a generator expression to compute the sum of the squares of all odd numbers 
from 1 through 100, without constructing an intermediate list. The expression should 
look like sum(x*x for x in range(1, 101) if x % 2).
"""
def main():
    print("the sum is:", sum(generator_expression()))

def generator_expression():
    for i in range(1, 100):
        if (i % 2 > 0): 
            yield i ** 2
if __name__ == "__main__":
    main()