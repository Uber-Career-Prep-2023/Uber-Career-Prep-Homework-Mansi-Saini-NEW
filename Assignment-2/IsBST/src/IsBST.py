# Question: IsBST
# Technique Used: Depth-first Search
# Time Complexity: O(n) - dependent on number of nodes
# Space Complexity: o(n) - dependent on number of nodes
# Time Spent: 65 min 

# Directions: Given a binary tree, determine if it is a binary search tree.

# Node class
class Node:
    def __init__(self, val) -> None:
        self.left = None
        self.right = None
        self.val = val

"""
    Goal: given a binary search tree, determine if it is a binary search tree.
    Parameters: binary search tree instance
    Output: boolean value: true if BST, false if not BST
"""
def IsBST(root):
    # base case: empty bst - technically a BST
    if root is None:
        return True
    
    # call to helper function to validate bst - pass in int_min and int_max
    return validate_bst(root, float("-inf"), float("inf"))

"""
    Goal: Check for a valid left or right side of bst
    Parameters: root, left side of bst, right side of bst
    Output: recursive call to validate each node
"""
def validate_bst(node, left, right):
    # if no children exist, bst is validated
    if not node:
        return True
    
    # check if node's value is NOT within the conditions of a bst
    if not (node.val < right and node.val > left):
        return False
    # node's val is within conditions of bst
    # left side: search the left side, lower bound is the same, upper bound shrinks
    return validate_bst(node.left, left, node.val) and validate_bst(node.right, node.val, right)

# helper function to print values in the bst
# input: array values, and int root
# output: array of values in the tree
def print_tree(values, root):
    values.append(root.val) # add root's value to the output array

    # check if there is a left side of the tree
    if root.left:
        print_tree(values, root.left) # traverse left side and print

    # check if there is a right side of the tree
    if root.right:
        print_tree(values, root.right)
    
    return values # output values


if __name__ == "__main__":
    # Tests
    
    # define nodes
    node1 = Node(7)
    node2 = Node(4)
    node3 = Node(10)
    node4 = Node(3)
    node5 = Node(5)
    node6 = Node(8)
    node7 = Node(20)


    # set children
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7

    root = node1 # set root
    is_bst = IsBST(root) # make a deep copy of the bst

    print(is_bst) # is it a bst
    print(print_tree([], root)) # original bst: []

    """
                    7
                  /   \ 
                4       10
               / \     /  \ 
              3   5   8   20
    
    
    """
