import random
import math

"""
    Finds a given number in a list, returns its index if found or -1 if not found.
"""
def binary_search(list, to_find):
    min = 0
    max = len(list) - 1
    # counter = 1
    
    if to_find < list[min] or to_find > list[max]:
        return -1

    while(min <= max):
        mid = math.floor((min + max) / 2)
        # print(f"========== Attempt {counter} ==========")
        # print(f"min: {list[min]}")
        # print(f"max: {list[max]}")
        # print(f"to_find: {to_find}")
        # print(f"result: index {mid} - number {list[mid]}")
        
        if to_find == list[mid]:
            return mid
        
        # counter += 1
        if (nums[mid] > to_find):
            max = mid - 1
        else:
            min = mid + 1
        
    return -1
    
# Test
if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    min = 0
    max = len(nums) - 1

    selection = random.randint(nums[min], nums[max])
    answer = binary_search(nums, selection)

    print("============================")
    print(f"answer: {answer}")
