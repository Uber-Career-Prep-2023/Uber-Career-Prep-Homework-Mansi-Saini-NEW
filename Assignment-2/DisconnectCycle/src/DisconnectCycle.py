# Question: DisconnectCycle
# Technique Used: Linked list fast-slow pointer
# Time Complexity: O(n)
# Space Complexity: O(1) - constant space
# Time Spent: 35 min

class Node: 
    def __init__(self, val) -> None:
        self.next = None
        self.val = val
    
class LinkedList:
    def __init__(self, val) -> None:
        self.head = val

    """
        Goal: Find a cycle within a linked list
        Params: head of linked list
        Output: meeting point of fast and slow pointers
    """
    def find_cycle(self):
        # init slow, fast pointers
        slow = self.head
        fast = self.head
        
        # traverse until fast and slow pointer are at same location
        # fast ptr will eventually catch up to the slow pointer
        # continue until you reach the end of linked list (if exists)
        while slow.next != None and fast.next.next != None: 
            # update slow and fast ptrs
            slow = slow.next
            fast = fast.next.next

            # ptrs are at same location; return meeting point
            if slow == fast:
                print("Meeting point: ", fast.val)
                return fast
    
    """
        Goal: Cut off cycle within the linked list
        Params: meeting point of fast and slow pointers
        Output: Linked list with removed cycle
    """
    def cut_cycle(self, meeting_pt):
        prev = None # keep track of previous ptr from meeting
        curr = self.head # ptr at front of linked list

        # continue traversing until meeting and init ptr meet
        while meeting_pt != curr:
            # update ptrs
            curr = curr.next
            prev = meeting_pt
            meeting_pt = meeting_pt.next
        print("Curr: ", curr.val, "Prev: ", prev.val)
        prev.next = None # set previous of meeting ptr to null to break cycle
    
    """
        Goal: Given a singly linked list, disconnect the cycle, if one exists.
        Params: linked list
        Output: cycle-detached linked list (if exists)
    """
    def DisconnectCycle(self):
        # edge case: empty linked list
        if self.head is None:
            return

        meeting_pt = self.find_cycle() # call to helper function find cycle

        self.cut_cycle(meeting_pt) # call to cut off cycle helper function

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

    test_list.head = Node(10)
    test_list.head.next = Node(18)
    test_list.head.next.next = Node(12)
    test_list.head.next.next.next = Node(9)
    test_list.head.next.next.next.next = Node(11)
    test_list.head.next.next.next.next.next = Node(4)
    # cycle
    test_list.head.next.next.next.next.next.next = test_list.head.next.next.next.next.next
    print("_________Original LIST__________________")
    # test_list.print_llist()
    # uncomment for endless cycle printing

    print("___________Disconnect cycle______________")
    test_list.DisconnectCycle()
    test_list.print_llist()


    
    
        
        
    
