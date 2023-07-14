# create node in tree
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None # left node
        self.right = None # right node

# create binary search tree class
class BinarySearchTree:
    def __init__(self, val):
        self.root = Node(val)

    """
    Goal: returns the minimum value in the binary search tree
    Parameters: binary search tree instance
    Output: int - minimum value
    
    """
    def min(self): # returns the minimum value in the BST
        # edge case: empty BST
        if self.root is None:
            return
        # create current node
        curr = self.root # set to root of bst
        # go through left side of bst
        while curr.left is not None:
            curr = curr.left
        # until you reach the leaf and return it
        return curr.val # left most val in bst
    
    """
    Goal: returns the maximum value in the binary search tree
    Parameters: binary search tree instance
    Output: int - maximum value
    
    """
    def max(self): # returns the maximum value in the BST
        # max value will be the rightmost value, so we can continue searching on the right side
        # edge case: empty BST
        if (self.root is None):
            return
        curr = self.root # current node
        while curr.right is not None: # traverse to right end
            curr = curr.right
        return curr.val

    """
    Goal: check if binary search tree exists; calls helper _contains function
    Parameters: binary search tree instance and int value to search for in the tree
    Output: bool - if value is not in BST or call to helper function _contains
    
    """
    def contains(self, val): # returns a boolean indicating whether val is present in the BST
        # edge case check: bst is empty
        if self.root is None:
            return False
        else:
            self._contains(val, self.root) # go through helper function

    """
    Goal: 
        - helper function to the contains function
        - returns a boolean value if the value is present in the binary search tree or not
    Parameters: 
        - binary search tree instance, int value to search for, and node in BST
    Output: 
        - bool val - True if value exists in BST and False if value doesn't exist in BST
    
    """
    # helper function to check if value is contained in bst
    def _contains(self, val, node):
        # traverse bst
        # check if value is less than current node value,
        if (node.val > val):
            if (node.left is None): # value doesn't exist
                return False
            self._contains(val, node.left) # if so, check left side
            
        elif (node.val < val): # check if value is greater than current node value 
            if (node.right is None): # value doesn't exist
                return False
            self._contains(val, node.right) # if so, check right side
        elif (node.val == val): # value exists in bst
            return True
        return False

    """
    Goal: call to helper function to_insert if there is exists a binary search tree
    Parameters: 
        - binary search tree instance, int value to insert in the tree
    Output: 
        - the input value if the tree is empty or call to the helper to_insert function
    
    """
    # For simplicity, do not allow duplicates. If val is already present, insert is a no-op
    def insert(self, val): # creates a new Node with data val in the appropriate location
        # edge case: empty bst
        if self.root is None:
            return Node(val) # set input val as the root of the bst
        else:
            self.to_insert(val, self.root)

    """
    Goal: inserts an integer value in the binary search tree 
    Parameters: 
        - binary search tree instance, int value to search for, and node in BST
    Output: 
        - nothing, solely insert the value into the binary search tree
    
    """
    # helper function for insertion
    def to_insert(self, val, node):    
        # traverse bst
        # if 'value to insert' is smaller than the current value in the bst
        if (node.val > val):
            if node.left is None: # see if there is no child
                node.left = Node(val) # insert node
            # if a left side exists, traverse the left side
            else:
                self.to_insert(val, node.left)

        # if a right side exists, traverse the right side
        elif (node.val < val):
            if node.right is None: # if no child exists
                node.right = Node(val) # insert value
            else: # there must be a right side to search, so search it
                self.to_insert(val, node.right)
        elif (node.val == val):
            return # do not insert duplicates

    """
    Goal: make sure there exists a binary search tree to delete something 
    Parameters: 
        - binary search tree instance, int value to delete
    Output: 
        - call to helper function if there exists something to delete
    """
    def delete(self, val): # deletes the Node with data val, if it exists
        # edge case: empty bst
        if (self.root is None):
            return Node(val) # nothing to delete
        else:
            return self._delete(val, self.root)
    
    """
    Goal: helper function to delete value in the binary search tree 
    Parameters: 
        - binary search tree instance, int value to delete, and node
    Output: 
        - return remaining elements of binary search tree
    """
    # helper function to delete value out of bst
    def _delete(self, val, node):
        print("CURRENT VAL IN TREE: ", node.val)
        print("VALL: ", val)
        # if value is smaller than the current node; search the left side
        if (node.val > val):
            if node.left is None: # check if there is no child
                return # nothing to delete
            self._delete(val, node.left) # search left side
        elif (node.val < val): # if value is larger than the current ndoe; search the right side
            if (node.right is None): # check if there is no child
                return # nothing to delete
            self._delete(val, node.right) # search right side
        else: # if the current value is the same value
            if node.left is None: # node has no child
                tmp = node.right # store right children
                node = None 
                return tmp 
            elif node.right is None: # node has no child
                tmp = node.left # store left children
                node = None
                return tmp

def main():
    # Test Cases
    tree = BinarySearchTree(5)

    """ Let us create following BST
               5
            /     \
           2       10
          /  \    /  \
         1    3  9   30 """

    # INSERT INTO BST
    tree.insert(3) # duplicate test
    tree.insert(3)
    tree.insert(9)
    tree.insert(1) # duplicate test
    tree.insert(1)
    tree.insert(30)
    tree.insert(10)
    tree.insert(2)

    # MIN
    print("MIN: ", tree.min())
    # MAX
    print("MAX: ", tree.max())

    # DELETE
    tree.delete(1)
    tree.delete(3)
    print("WE DELETED 1 and 3")

    # MIN
    print("MIN: ", tree.min())
    # MAX
    print("MAX: ", tree.max())

    # CONTAINS
    tree.contains(1)
    tree.contains(232)


# to make sure main is executed
if __name__ == '__main__':
    main()

