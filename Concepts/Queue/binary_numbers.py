"""
3 ----
Generate binary numbers from 1 to N using a queue
Input: N=5 → Output: ['1', '10', '11', '100', '101']
"""
def main():
    # 1 10, 11, 100, 101, 110, 111, 1000, 1001, 1010
    # n_number = int(input("Enter a n number: "))
    print(" ".join(str(n) for n in bin_sequence_to(4)))

# def generate_binary_sequence_to(number : int) -> list:

def bin_sequence_to(long):
    if long == 0:
        yield ""
    else:
        for prefijo in bin_sequence_to(long - 1):
            yield prefijo + "0"
            yield prefijo + "1"

if __name__ == "__main__":
    main()