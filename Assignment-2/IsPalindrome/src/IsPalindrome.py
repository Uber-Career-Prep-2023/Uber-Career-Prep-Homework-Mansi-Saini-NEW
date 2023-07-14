# Question: IsPalindrome
# Technique Used: Doubly linked list forward-backward two-pointer
# Time Complexity: O(n) + O(n/2) -> ~O(n)
            # find tail and check palindrome until middle
# Space Complexity: O(1) - constant time
# Time Spent: 11 min

# Directions: Given a doubly linked list, determine if it is a palindrome.

# Node Class
class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None
        self.prev = None

# Linked list class
class LinkedList:
    def __init__(self, val) -> None:
        self.head = val

    """
        Goal: given a doubly linked list, determine if it is a palindrome
        Params: linked list
        Output: boolean
    """
    def isPalindrome(self):
        # edge case check: empty linked list
        if self.head is None:
            return True

        tail = self.head

        # traverse to right end and get tail
        while tail.next is not None:
            tail = tail.next
        
        front = self.head

        # traverse until the front and tail are equal
        while front != tail: 
            # if the tail is equal to the front
            if tail.val == front.val:
                # update front and tail - move inwards
                front = front.next
                tail = tail.prev
                continue
            # otherwise, immediately return false
            return False
        return True # made it through palindrome check
    
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

if __name__ == "__main__":

    llist = LinkedList(2)
    llist.head = Node(9)
    llist.head.next = Node(12)
    llist.head.next.prev = llist.head
    llist.head.next.next = Node(4)
    llist.head.next.next.prev = llist.head.next
    llist.head.next.next.next = Node(2)
    llist.head.next.next.next.prev = llist.head.next.next
    llist.head.next.next.next.next = Node(9)
    llist.head.next.next.next.next.prev = llist.head.next.next.next
    print("_________Original LIST__________________")
    llist.print_llist()
    
    print(llist.isPalindrome())