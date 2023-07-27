# Given a two dimensional array that contains only 0s and 1s, and all 0s come before all 1s in any given row. 
# Find the first column containing a 1. 


# Example input:
#         n
#    0, 0, 0, 0, 1, 1, 1
# m  0, 0, 1, 1, 1, 1, 1
#    0, 0, 0, 0, 0, 0, 0

# Example output : 2
# Approach: Linear Search
# Time Complexity: O(n) - worse case
# Space Complexity: O(1) - just searching

def first_one(arr):
    # edge case: empty arr
    if len(arr) <= 0:
        return

    # store the rows, columns, and earliest column to output
    row = 0
    col = 0 
    earliest_col = len(arr[0])

    # edge case: empty subarrays
    if col < 0:
        return

    # continue iterating through while the rows and columns are valid
    while (row < len(arr) and col < earliest_col):
        # if we hit a one
        if (arr[row][col] == 1):
            # update the earliest column idx if earlier than the previous column
            if (col < earliest_col):
                earliest_col = col
            # move down (increase row)
            row += 1
            col = 0 # reset columns
        # otherwise, its a 0, so we can move to the right (increase column)
        elif (col < len(arr[0]) - 1):
            col += 1
        else: # reached end of a row without any 1s
            col = 0
            row += 1

    # edge case: no 1s present
    if (earliest_col < 0 or earliest_col == len(arr[0])):
        return

    # output earliest column
    return earliest_col

# test cases 

print(first_one([[0, 0, 0, 0, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0]])) # output: 2
print(first_one([[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1]]))
print(first_one([]))
print(first_one([[],[],[]]))
print(first_one([[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]))