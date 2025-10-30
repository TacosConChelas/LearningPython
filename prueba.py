def rotate(nums : list, k : int):
    # write your function here...
    if k == 0:
        return nums
    for _ in range(k):
        nums[0], nums[-1] = nums[-1], nums[0]
    return nums
def main():
    nums = [10, 20, 30, 40, 50]
    text = (map(lambda x: str(x), rotate(nums, 2)))
    print(" ".join(text))
main()
    