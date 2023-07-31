# Question: FloorInBST
# Technique Used: 
# Time Complexity: 
# Space Complexity: 
# Time Spent: 
# start: 4:42 pm (5 min buffer)

# Given a target numeric value and a binary search tree, return the floor (greatest element less than or equal to the target) in the BST.



# BST Node Class
class Node:
    def __init__(self, val) -> None:
        self.left = None
        self.right = None
        self.val = val
    
# BST class
class BinarySearchTree:
    def __init__(self, val) -> None:
        self.root = Node(val) # root of BST

    """
        Goal: Return the floor (greatest element less than or equal to the target) in the BST.
        Params: BST root, int target value
        Output: int floor of closest value to target
    """
    def floorInBST(self, root, target):
        # edge case: empty BST
        if root is None:
            return        

        # base case: if the rootent value is equal to the target
        if root.val == target:
            return root.val # immediately return the value
        # if target is less than rootent value and children exist
        if root.val > target:
            return self.floorInBST(root.left, target) # recursive search left side of BST

        # if target is greater than rootent value and children exist
        if root.val < target:
            right_subtree = self.floorInBST(root.right, target)
            # check if right child exists and if target is greater than right value
            if right_subtree != None and right_subtree <= target:
                return right_subtree # continue searching

        return root.val
    
    
                

if __name__ == "__main__":

    # build BST
    test_BST = BinarySearchTree(2)
    test_BST.root = Node(10)
    test_BST.root.left = Node(8)
    test_BST.root.left.left = Node(3)
    test_BST.root.left.left.left = Node(2) # min value in BST
    test_BST.root.left.right = Node(9)
    test_BST.root.right = Node(16)
    test_BST.root.right.left = Node(13)
    test_BST.root.right.right = Node(17)
    test_BST.root.right.right.right = Node(20) # max value in BST

    # Test Cases
    assert test_BST.floorInBST(test_BST.root, 15) == 13
    assert(test_BST.floorInBST(test_BST.root, 13)) == 13
    assert(test_BST.floorInBST(test_BST.root, 1000)) == 20