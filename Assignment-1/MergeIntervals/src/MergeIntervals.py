# Question: MergeIntervals
# Technique Used: Sort then solve
# Time Complexity: O(nlogn) - due to initial sorting
# Space Complexity: O(n) - creation of arrays
# Time Spent: 40 min - Finished!

# Directions: Write a function that addresses the
# following problem and define test cases
# to check the function itself

# Given a list of integer pairs representing the low 
# and high end of an interval, inclusive, return a list 
# in which overlapping intervals are merged.

# Thought Process
    # Would be easier if intervals were sorted
    # sort them in increasing order
    # convert list of tuples to list of lists

    # create array for merged intervals
    # include the first interval in the merged intervals array
    # (1, 2)
    # (1, 2)(2, 3)(4, 8)(5, 7), (9, 12)
    # traverse sorted intervals array
        # check if current interval 1 is greater than or equal to merged interval 1 (Greater than minimm of interval - within range on lower bound)
        # and check if current interval 1 is less than or equal to merged interval 2 (smaller than max range) 
            # if so,
                # new merged interval in array is (the original first minimum, max(merged interval2, current interval 2))
        # otherwise, we cannot merge the intervals
            # have to add to our output array without merging
    # convert merged array back to a list of tuples
    # return the output array of merged intervals

def MergeIntervals(arr):
    arr = sorted(arr) # sort input array
    intervals = list(map(list, arr)) # convert list of tuples to lists of lists
    merged = [] # create output merged intervals array

    merged.append(intervals[0]) # include first interval to begin
    for i in intervals[1:]: # traverse input interval array
        # check if can merge intervals together - most recent element in merged array
        if (i[0] >= merged[-1][0] and i[0] <= merged[-1][-1]): 
            # add max upper bound out of merged array and interval array
            merged[-1][-1] = max(merged[-1][-1], i[-1])
        else:
            # otherwise add interval to merged array separately
            merged.append(i)
    merged = list(map(tuple, merged)) # convert lists of lists back to a list of tuples
    return merged # return list of merged intervals



# Tests
MergeIntervals([(0, 0)])
MergeIntervals([(2, 3), (4, 8), (1, 2), (5, 7), (9, 12)])
MergeIntervals([(5, 8), (6, 10), (2, 4), (3, 6)])
MergeIntervals([(10, 12), (5, 6), (7, 9), (1, 3)])
