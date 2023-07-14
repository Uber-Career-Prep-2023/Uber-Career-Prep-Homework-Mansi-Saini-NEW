 # Question: MaxMeanSubArray
# Technique Used: Variable-size (shrinking/growing) sliding Window
# Time Complexity: O(n)^3
# Space Complexity: O(n)
# Time Spent: 65 min (Finished)!

# Directions: Write a function that addresses the
# following problem and define test cases
# to check the function itself

# Thought Process
    # flexible sliding window
    # store count of subarrays that sum to 0
    # traverse the array
    # have two pointers that init point to beginning
    # keep one fixed
    # use the second to extend subarray until we hit the array end
    # check if current subarray sums to zero
    # once we hit the end, shift fixed over by one; reset dynamic
    # and repeat

def ZeroSumSubArrays(input):
    count = 0
    left = 0
    right = len(input) - 1
    sum = 0
    for y in range(len(input) -1 ):
        for i in range(len(input) - 1): # traverse array
            for x in range(left, right + 1): # traverse subarray
                sum += input[x] #  add to sum of subarray
            if (sum == 0):
                count += 1
            right -= 1
            sum = 0

            # should not reach range of (2, 1); stop at (2, 2)
            if (left == right):
                break
        left += 1
        right = len(input) - 1
    count += input.count(0) # take into account [0] case
    print("final count: ", count)
    return count
        


ZeroSumSubArrays([4, 5, 2, -1, -3, -3, 4, 6, -7])
ZeroSumSubArrays([1, 8, 7, 3, 11, 9])
ZeroSumSubArrays([8, -5, 0, -2, 3, -4])

