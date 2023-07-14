# Question: DedupSortedList
# Technique Used: reset/catch-up two pointer linked list
# Time Complexity: O(n)
# Space Complexity: O(n)
# Time Spent: 40+ min

# Directions: Given a sorted singly linked list, remove any duplicates so that no value appears more than once.

# Node class
class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

# Linked List class
class Llist:
    def __init__(self, val) -> None:
        self.head = val

    """
        Goal: Given a sorted singly linked list, remove any duplicates so that no value appears more than once.
        Parameters: linked list
        Output: removed duplicates linked list
    """
    def DedupSortedList(self):
        # edge case: empty linked list

        curr = self.head.next # store current node
        prev = self.head # store previous node

        # traverse linked list until empty
        while curr is not None:
            if curr.val != prev.val:
                prev.next = curr
                prev = curr
            curr = curr.next
        # return the same array
        return self.head

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

if __name__ == '__main__':
    test_list = Llist(3)

    test_list.head = Node(2)
    test_list.head.next = Node(3)
    test_list.head.next.next = Node(4)
    test_list.head.next.next.next = Node(4)
    test_list.head.next.next.next.next = Node(5)
    test_list.head.next.next.next.next.next = Node(5)
    test_list.head.next.next.next.next.next.next = Node(8)
    print("_________Original LIST__________________")
    test_list.print_llist()
    # [2, 3, 4, 4, 5, 5, 6, 7, 8]

    # DELETE DUPLICATES
    print("__________new list_______________")
    test_list.DedupSortedList()
    test_list.print_llist()
    




