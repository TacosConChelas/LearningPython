from collections import deque

def generate_binary_numbers(n: int) -> list[str]:
    if n <= 0:
        return []

    result = []
    queue = deque()
    queue.append("1")

    for _ in range(n):
        # Step 1: Pop front
        front = queue.popleft()
        result.append(front)

        # Step 2: Generate next two and enqueue
        queue.append(front + "0")
        queue.append(front + "1")

    return result


def main():
    n = 4
    print(generate_binary_numbers(n))

if __name__ == "__main__":
    main()
