# Question: MergeKSortedArrays
# Technique Used: Heap
# Time Complexity: log(n) + O(n^2) - heap time complexity and going through arrays and array elements
# Space Complexity: O(n)
# Time Spent: 40 min

import heapq

"""
    Goal: Given an array of k sorted arrays, merge the k arrays into a single sorted array.
    Parameters:  array of k sorted arrays
    Output: merged array
"""
def MergeKSortedArrays(k, arrs):
    # edge case check: no arrays given
    if arrs is None:
        return 
    
    # edge case check: invalid k value
    if k < 0:
        return

    minheap_contains = [] # store what minheap contains
    merged_arr = [] # output array
    for i in arrs: # go through the arrays
        for elem in i: # go through each element in array
            heapq.heappush(minheap_contains, elem) # add elements to minheap
    while minheap_contains: # continue until minheap is empty
        merged_arr.append(heapq.heappop(minheap_contains)) # pop the smallest value and add to output array
    return merged_arr


# Test Cases
if __name__ == "__main__":
    # print(MergeKSortedArrays(2, [[1, 2, 3, 4, 5], [1, 3, 5, 7, 9]]))
    assert MergeKSortedArrays(2, [[1, 2, 3, 4, 5], [1, 3, 5, 7, 9]]) == [1, 1, 2, 3, 3, 4, 5, 5, 7, 9]

    # print(MergeKSortedArrays(3, [[1, 4, 7, 9], [2, 6, 7, 10, 11, 13, 15], [3, 8, 12, 13, 16]]))
    assert MergeKSortedArrays(3, [[1, 4, 7, 9], [2, 6, 7, 10, 11, 13, 15], [3, 8, 12, 13, 16]]) == [1, 2, 3, 4, 6, 7, 7, 8, 9, 10, 11, 12, 13, 13, 15, 16]
    