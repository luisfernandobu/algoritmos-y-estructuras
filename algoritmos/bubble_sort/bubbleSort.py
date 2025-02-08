import random

"""
    Sorts a list of numbers using the bubble sort algorithm.
"""
def bubble_sort(nums):
    nums_len = len(nums)
    sort = True
    
    while(sort):
        sort = False
        for i in range(nums_len - 1):
            num1 = nums[i]
            num2 = nums[i + 1]
            
            if (num1 > num2):
                sort = True
                nums[i] = num2
                nums[i+1] = num1
                
    return(nums)

# Test
if __name__ == '__main__':
    nums = []
    for n in range(10):
        nums.append(random.randint(1, 100))
    print("unsorted nums: ", nums)
    
    sorted_nums = bubble_sort(nums)
    print("sorted nums: ", sorted_nums)