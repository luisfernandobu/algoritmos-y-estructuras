import random
import math

"""
    Finds a given number beetwen a range and counts the attempts to find it.
"""
def binary_search(min, max, selection):
    if selection < min or selection > max:
        return -1
    
    counter = 1
    result = math.floor(max/2) # first try
    print_result(counter, min, max, selection, result)

    while(selection != result):
        counter += 1

        if (result > selection):
            max = result - 1
        else:
            min = result + 1
        
        result = math.floor((min+max)/2)
        print_result(counter, min, max, selection, result)
    
    return result

def print_result(counter, min, max, selection, result):
    print(f"========== Attempt {counter} ==========")
    print(f"min: {min}")
    print(f"max: {max}")
    print(f"selection: {selection}")
    print(f"result: {result}")

# Test
if __name__ == "__main__":
    min = 1
    max = 2539913
    selection = random.randint(min, max)
    
    binary_search(min, max, selection)
