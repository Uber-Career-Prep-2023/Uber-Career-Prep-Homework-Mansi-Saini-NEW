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
    # edge case: empty bst
    if root is None:
        return

    # create a priority queue for nodes
    queue = [root]

    # create an output array
    out = []

    # continue traversing while there are still nodes to process
    while (queue):
        # create the current level: would be length of nodes to process
        curr_level = len(queue)

        # go through the current level of nodes until there are none
        for i in range(curr_level):
            # pop the first node off to process
            
            curr_node = queue.pop(0)

            # the first value will be the 'left view' (iterator is at 0 in the level)
            if i == 0:
                # so we append to the output array
                out.append(curr_node.val)
            
            # if there exists a left subtree, add to nodes to process
            if curr_node.left:
                queue.append(curr_node.left)

            # if there exists a right subtree, add to nodes to process
            if curr_node.right:
                queue.append(curr_node.right)
    
    # return output array
    return out

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
    