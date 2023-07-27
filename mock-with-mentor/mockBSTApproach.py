# Given a two dimensional array that contains only 0s and 1s, and all 0s come before all 1s in any given row. 
# Find the first column containing a 1. 


# Example input:
#         n
#    0, 0, 0, 0, 1, 1, 1
# m  0, 0, 1, 1, 1, 1, 1
#    0, 0, 0, 0, 0, 0, 0

# Example output : 2
# Approach: Binary Search
# Time Complexity: O(n log m)
# Space Complexity: O(1) - purely just searching through arr

def first_one(arr):
    # edge case: empty array
    if len(arr) == 0:
        return

    # store the earliest column
    earliest_col = len(arr[0])

    row = 0
    col = len(arr[0]) - 1

    # edge case: empty subarrays
    if col < 0:
        return

    # continue while columns are greater than 0 and rows are less than the column length
    while (col >= 0 and row < len(arr)):
        # base case: if the current val is a 0
        if arr[row][col] == 0:
            # update row to next one (+1)
            row += 1
        # otherwise, must be a 1
        else:
            # store the current column index
            earliest_col = col
            # update column to one to the left(-1)
            col -= 1

    # edge case: no 1s present
    if (earliest_col >= len(arr)):
        return

    # output earliest column
    return earliest_col

# test cases 

print(first_one([[0, 0, 0, 0, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0]])) # output: 2
print(first_one([[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1]]))
print(first_one([]))
print(first_one([[],[],[]]))
print(first_one([[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]))