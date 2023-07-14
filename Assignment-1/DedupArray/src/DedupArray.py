# Question: DedupArray
# Technique Used: Set Conversion
# Time Complexity: O(n)
# Space Complexity: O(1) - modifying original array
# Time Spent: 10 min - Finished!

# Directions: Write a function that addresses the
# following problem and define test cases
# to check the function itself

# Given a sorted array of non-negative integers, 
# modify the array by removing duplicates so each 
# element only appears once. If arrays are static 
# (aka, not dynamic/resizable) in your language of c
# hoice, the remaining elements should appear in the 
# left-hand side of the array and the extra space in the 
# right-hand side should be padded with -1s.


# Thought Process

    # WORSE SPACE COMPLEXITY
    # create a visited array
    # traverse input array
        # see if current element is in visited array
            # if so, skip element
        # if current element is not in visited arary
            # add to visited array
    # return visited array that doesn't have duplicates

    # MORE OPTIMAL COMPLEXITY (TIME AND SPACE)
    # convert array to a set and return as a list
    

def DedupArray(arr):
    arr = set(arr) # convert array to a set to remove duplicates
    return list(arr) # return set as an array without duplicates

# Tests

DedupArray([])
DedupArray([1, 0, 0, 0, 0])
DedupArray([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
DedupArray([0, 0, 1, 4, 5, 5, 5, 8, 9, 9, 10, 11, 15, 15])
DedupArray([1, 3, 4, 8, 10, 12])