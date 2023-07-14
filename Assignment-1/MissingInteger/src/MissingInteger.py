# Question: MissingInteger
# Technique Used: Binary Search
# Time Complexity: O(nlogn)
# Space Complexity: O(1)
# Time Spent: 40 min - Finished!
    
# Directions: Write a function that addresses the
# following problem and define test cases
# to check the function itself

# Thought Process
    # Initial Approach - 10 minutes
    # binary search is possible; starting with iterative approach, then will optimize if extra time
        # convert arr to a set
        # intersection range from first element to last and input array
        # return intersected element   

    # Optimized Approach - 30 min
        # each element in array should be the index value + 1 (e.g arr[0] should have value 1, arr[1] should have value 2)
        # edge case check; emtpy array and array of length 1
        # binary search
            # create left which is beginning of array
            # create right which is end of array
                # continue until the left side is greater than the right - pointers cross
                # set the middle as the addition of the left and right side // 2 to split into smaller ranges
                    # if the middle value is equal to its index value + 1
                        # search the right side; we know that middle is in the right place of array, so missing is on the right
                        # set left as the middle
                    # otherwise, middle value is not in correct spot (doesn't follow index value + 1)
                        # search the left side
                        # set right as the middle

                
 
def MissingInteger(arr, n):

    # OPTIMIZED APPROACH - binary search
    if (len(arr) == 0): # edge case: empty array
        print(1)
        return 1 # only 1 element in range
    if (len(arr) == 1): # edge case: array of length 1
        print(2)
        return 2 # two elements in range
    
    left = 0 # left side of array
    right = n - 1 # right side of array
    mid = 0 # init middle of array

    while (left + 1 < right): # until left and right pointers cross each other
        mid = (left + right) // 2 # create middle of array
        if (arr[mid] == mid + 1): # middle value meets condition; search right side
            left = mid
        elif (arr[mid] != mid + 1):
            right = mid # middle value doesn't meet condition; search left side
    return(arr[left] + 1) # missing integer




    # # ONE VERSION THAT WORKS: conversion to set and find difference between set and array - 10 minutes
    # # edge case check: empty array
    # if (len(arr) == 0):
    #     return 1 # first element in range
    # if (len(arr) == 1): # edge case check: 1 element in array
    #     return 2 # second element in range
    # # find range from first element to end, convert range to a set and find the difference numbers between the range and the array
    # output = set(range(arr[0], n + 1)).difference(arr) 
    # missing = int(output.pop()) # pop missing number out of set
    # return missing


MissingInteger([], 1)
MissingInteger([1, 2, 3, 4, 6, 7], 7)
MissingInteger([1], 2)
MissingInteger([1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12], 12)
