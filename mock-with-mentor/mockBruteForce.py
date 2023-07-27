# Given a two dimensional array that contains only 0s and 1s, and all 0s come before all 1s in any given row. Find the first column containing a 1. 

# Example input:
#         n
#    0, 0, 0, 0, 1, 1, 1
# m  0, 0, 1, 1, 1, 1, 1
#    0, 0, 0, 0, 0, 0, 0

# Example output : 2

# Approach: Brute Force
# Time Complexity: O(n^2) - could be optimized
# Space Complexity: O(1) - just searching through

def first_one(arr):
    # edge case: empty arr
    if arr is None or len(arr) == 0:
        return None

    # create a variable for earliest column
    earliest_col = len(arr)

    # go through the rows and columns
    for m in range(len(arr)):
        for n in range(len(arr[0])):
            # continue until you hit a 1
            if (arr[m][n] == 1):
                # if the col position of the 1 is earlier current earliest col
                if (n < earliest_col):
                    # update earliest column
                    earliest_col = n
        # continue through
    # no ones present
    if (earliest_col == len(arr)):
        return None

    # return earliest column
    return earliest_col


# test cases
print(first_one([[0, 0, 0, 0, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0]])) # output: 2
print(first_one([[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1]]))
print(first_one([]))
print(first_one([[],[],[]]))
print(first_one([[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]))

