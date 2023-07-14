# Question: TwoSum
# Technique Used: Fixed Sliding Window
# Time Complexity: O(n) - single traversal throgh the array
# Space Complexity: O(n) - store frequencies in a dictionary
# Time Spent: 37 min - Finished!

# Directions: Write a function that addresses the
# following problem and define test cases
# to check the function itself

# Given an array of integers and a target integer, k, return 
# the number of pairs of integers in the array that sum to k.
# In each pair, the two items must be distinct elements (come 
# from different indices in the array).


# Thought Process
    # create an output counter
    # create empty dictionary 
    # traverse the array
        # see if the current value minus k (diff) exists in the dictionary
            # if so, increment output counter by how many times the diff appears in the dictionary
        # if the current value is already in the dictionary
            # increment the frequency of the current value
        # otherwise
            # set the frequency of the current value to one since it doesn't exit elsewhere
    # return output counter

def TwoSum(arr, k):
    output = 0 # init pair counter
    freq = {} # create dictionary to store frequencies

    # traverse the array
    for i in arr:
        if k - i in freq: # difference is in dictionary
            output += freq[k - i] # update output count 
        if i in freq: # current value is already in dictionary
            freq[i] += 1 # increment frequency by 1
        else: # first time current value or difference appear in dictionary
            freq[i] = 1 # must have a frequency of 1 only
              
    print("output: ",output)
    return output # return the final output

# Tests

TwoSum([1, 10, 8, 3, 2, 5, 7, 2, -2, -1], 10)
TwoSum([1, 10, 8, 3, 2, 5, 7, 2, -2, -1], 9)
TwoSum([4, 3, 3, 5, 7, 0, 2, 3, 8, 6], 6)
TwoSum([4, 3, 3, 5, 7, 0, 2, 3, 8, 6], 1)