# Question: MaxMeanSubArray
# Technique Used: Fixed-size sliding Window
# Time Complexity: O(n)
# Space Complexity: O(n)?
# Time Spent: 40 minutes

# Did not have enough time to account for edge cases:
    # empty array or inputs
    # invalid inputs
    # k value greater than length of array

# Directions: Write a function that addresses the
# following problem and define test cases
# to check the function itself

# Thought Process
    # traverse the array
    # sum the subarray
    # find the average of the subarray
    # if greater than current max, update current average max
    # otherwise, continue finding averages of subarrays
    # output the final max subarray average

def maxSubArray(arr, k):
    max_ave = 0
    average = 0
    tail = 0
    head = k
    sum = 0

    # traverse through entire array
    for i in range(len(arr) - (k - 1)):
        # traverse through subarray
        for x in range(tail, head):
            sum += arr[x]  # find sum of subarray

        average = sum/k  # find average

        if (average > max_ave):
            max_ave = average  # update new max

        # update head and tail
        head += 1
        tail += 1
        sum = 0
    return max_ave

# edge case check
# maxSubArray([1], 2)
# maxSubArray([], 0)
# maxSubArray([], 2)
maxSubArray([4, 5, -3, 2, 6, 1], 2)
maxSubArray([4, 5, -3, 2, 6, 1], 3)
maxSubArray([1, 1, 1, 1, -1, -1, 2, -1, -1], 3)
maxSubArray([1, 1, 1, 1, -1, -1, 2, -1, -1, 6], 5)
