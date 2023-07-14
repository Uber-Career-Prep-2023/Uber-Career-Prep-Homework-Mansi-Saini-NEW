# Question: MoveNthLastToFront
# Technique Used: Fixed Distance Two Pointer
# Time Complexity: O(n) - depends on number of nodes
# Space Complexity: O(1) - constant space
# Time Spent: 40 min

# Directions: Given a singly linked list, move the nth from the last element to the front of the list.

# Node Class
class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self, val) -> None:
        self.head = val

    # length helper function
    def length(self):
        if self.head is None:
            return 0
        
        curr = self.head
        length = 0

        while curr is not None: # traverse to end
            length += 1
            curr = curr.next

        return length

    # insert at front helper function

    """
        Goal: move the nth from the last element to the front of the list
        Parameters: kth value
        Output: None
    """
    def MoveNthLastToFront(self, k):
        
        # edge case empty linked list
        if self.head is None:
            return
        
        pos = self.length() - k + 1 # position of value to move to front
        curr_pos = 1
        curr = self.head
        prev = None

        # continue iteration until position
        while curr_pos != pos:
            curr_pos += 1 
            prev = curr
            curr = curr.next
                
        # reached the position
        # delete value from linked list
        prev.next = curr.next
        
        # insert at the front of the helper function
        curr.next = self.head
        self.head = curr
        
        

    """
        Goal: helper function to print the linked list
        Parameters: None
        Output: None, just print the linked list values
    """
    def print_llist(self):
        # edge case: linked list exists
        if self.head is None:
            print("EMPTY LINKED LIST")
            return
        
        curr = self.head # keep track of current node
        # linked list exists, so traverse it
        while (curr != None):
            print(curr.val) # print current value
            curr = curr.next # move to next node

# Test Cases
if __name__ == "__main__":
    test_list = LinkedList(1)

    test_list.head = Node(15)
    test_list.head.next = Node(2)
    test_list.head.next.next = Node(8)
    test_list.head.next.next.next = Node(7)
    test_list.head.next.next.next.next = Node(20)
    test_list.head.next.next.next.next.next = Node(9)
    test_list.head.next.next.next.next.next.next = Node(11)
    test_list.head.next.next.next.next.next.next.next = Node(6)
    test_list.head.next.next.next.next.next.next.next.next = Node(19)
    print("_________Original LIST__________________")
    test_list.print_llist()
    print("length: ", test_list.length())


    print("__________move the 7th element from the last element to the front of the list_______________")
    test_list.MoveNthLastToFront(7)
    test_list.print_llist()

