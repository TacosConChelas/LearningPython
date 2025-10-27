"""
3) Find the second largest number in a list of integers.
"""
def main():
   numbers_list = [1, 3, 4, 4, 6, 7, 8, 8, 9, 8]
   numbers_list.sort()
   for i in numbers_list[::-1]:
      if numbers_list[i] > numbers_list[i + 1]: 
         print(numbers_list[i])
         break 
      else: 
         continue
if __name__ == "__main__":
    main()