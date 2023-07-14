# Question: CopyTree
# Technique Used: Pre-order Traversal - Depth First Search
# Time Complexity: O(n) - based on number of nodes
# Space Complexity: O(n) - based on number of nodes
# Time Spent: 40+ min

# Directions: Given a binary tree, create a deep copy. Return the root of the new tree.

# node class

class Node: 
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


"""
    Goal: given a binary search tree, create deep copy
    Parameters: binary search tree instance
    Output: root of new tree
"""
def copyTree(root):
    # base case: empty bst
    if root is None:
        return None
    else: # bst is not empty
        # copy the root
        copy = Node(root.val)
        # copy the left subtrees
        copy.left = copyTree(root.left)
        # copy the right subtrees
        copy.right = copyTree(root.right)

        # return the new root
        return copy

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
    deep_copy_arr = copyTree(root) # make a deep copy of the bst

    print(print_tree([], deep_copy_arr))
    print(print_tree([], root)) # original bst: []

    """
                    7
                  /   \ 
                4       10
               / \     /  \ 
              3   5   8   20
    
    
    """
