# Question: LeftView
# Technique Used: Breadth-first search
# Time Complexity: O(n)
# Space Complexity: O(n)
# Time Spent: 40 min

class Node: 
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None
    

"""
    Goal: Given a binary tree, create an array of the left view (leftmost elements in each level) of the tree.
    Params: binary tree
    Output: array of left view of bst
"""
def leftView(root):
    # edge case check: empty bst
    if root is None:
        return []
    
    # init output array + queue
    output = []
    nodes_to_process = [root]

    # continue until finished with bst
    while nodes_to_process:
        curr_level = len(nodes_to_process)
        
        # go through vals in the same level
        for i in range(curr_level):
            # get the first node to process
            node = nodes_to_process.pop(0)

            # first value will be left view
            if i == 0:
                output.append(node.val)
            
            # rest of nodes in bst
            if node.left is not None:
                nodes_to_process.append(node.left)
            
            if node.right is not None:
                nodes_to_process.append(node.right)
        
    return output

# TEST CASES
root = Node(7)
root.left = Node(8)
root.right = Node(3)
root.right.left = Node(9)
root.right.right = Node(13)
root.right.left.left = Node(20)
root.right.right.left = Node(14)
root.right.right.left.right = Node(15)

# PRINT THE LEFT VIEW
print(leftView(root))
# [7,8,9,20,15]
    