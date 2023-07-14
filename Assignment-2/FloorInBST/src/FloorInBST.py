# Question: FloorInBST
# Technique Used: Binary Search (keep narrowing down search)
# Time Complexity: O(n)
# Space Complexity: O(n)
# Time Spent: 37 min


class Node: 
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None
    

"""
    Goal: Given a target numeric value and a binary search tree, return the floor (greatest element less than or equal to the target) in the BST.
    Params: target value and binary tree
    Output: closest value to target value
"""
def FloorInBST(root, target):
    # edge case check: empty BST
    if root is None:
        return None
    
    # base case: root is target
    if root.val == target:
        return root.val
    
    # easier recursive case: current is greater than target
    if root.val > target:
        return FloorInBST(root.left, target)
    
    # harder recursive case: current is smaller than target - need to keep in mind floor
    if root.val < target:
        floor_helper = FloorInBST(root.right, target)
        if floor_helper != None and floor_helper <= target:
            return floor_helper
    
    # return closest val
    return root.val


# TEST CASES
root = Node(10)
root.left = Node(8)
root.right = Node(16)
root.left.right = Node(9)
root.right.left = Node(13)
root.right.right = Node(17)
root.right.right.right = Node(20)

# PRINT FLOOR IN BST 
print(FloorInBST(root, 14))

# [7,8,9,20,15]
    