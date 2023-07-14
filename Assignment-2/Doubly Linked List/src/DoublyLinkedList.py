# create Node class
class Node:
    # create node object
    def __init__(self, val):
        self.val = val  # assign data value
        self.next = None  # set head to null
        self.prev = None # set previous node to null

# create Linked List (llist)


class DoublyLinkedList:
    # initialize linked list head
    def __init__(self, val):
        self.head = None

    # Time Complexity: O(1) - no matter size, will place node at front
    # Space Complexity: O(1) - no extra space needed
    # creates new Node with data val at front; returns new head
    def insertAtFront(self, val):  # initialize new head node
        new_head = Node(val)  # initialize new node that stores data

        # edge case check: empty linked list
        if self.head is None:
            self.head = new_head
            return new_head

        # attach node to front of list; head might be empty if empty llist
        new_head.next = self.head # attach to front of linked list
        self.head.prev = new_head # attach old head to end of new head
        self.head = new_head  # update pointer to head to new node
        return new_head  # return new head

    # Time Complexity: O(n) - traverse entire llist to find its end and attach new node
    # Space Complexity: O(n) - have to store current val until end; dependent on llist size
    # creates new Node with data val at end
    def insertAtBack(self, val):
        curr = self.head  # set current node to front of llist
        while curr.next is not None:         # go through linked list until next node is end of llist
            curr = curr.next             # not end, update current node to next node

        # last element in linked list points to new node (new_tail)
        curr.next = Node(val)


    # Time Complexity: O(1) - linear time
    # Space Complexity: O(1) - same time no matter size of llist
    # creates new Node with data val after Node loc
    def insertAfter(self, val, loc):

        to_insert = Node(val) # init new node to insert
        to_insert.next = loc.next # link new node to front of loc's next node
        if loc.next != None: # if location to insert after isn't the end
            loc.next.prev = to_insert # link loc's node back to the node to insert
        loc.next = to_insert # set location's next ptr to point at node to insert
        to_insert.prev = loc # set previous pointer of insertion node    

    # Time Complexity: O(1); linear time
    # Space Complexity: O(1); delete from front; same for all sizes
    # removes first Node; returns new head
    def deleteFront(self):
        # edge case: empty llist
        if self.head is None:
            # return empty llist
            return

        new_head = self.head.next # set new head of llist to the next node
        self.head.next = None # break head from next node
        self.head = new_head # set new head
        return new_head
        
    
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # removes the last node
    def deleteBack(self):
        if self.head.next is None: # edge case check: empty linked list
            return None# nothing to delete

        curr = self.head # store current value of linked list
        while curr.next.next is not None: # continue until one before the end of linked list
            curr = curr.next # update current node to next one

        # detach one node from linked list
        curr.next = None # set new end pointer of linked list

    # Time Complexity: O(n) - depends on linked list size
    # Space Complexity: O(n) - shifting nodes requires temp storages
    # delete Node loc; returns head
    def deleteNode(self, loc):
        if loc == 0: # edge case check: empty linked list
            return self.deleteFront() # nothing to delete        
        curr = self.head # create current pointer
        prev_node = None # previous node
        curr_loc = 0 # create current location index counter
        
        while curr_loc < loc: # continue until we reach loc node; kth index node
            prev_node = curr # update prev node to current location
            curr = curr.next # update current node to next node over
            curr_loc += 1
        
        # reached the node to delete

        # make sure previous node exists
        if (prev_node != None):
            prev_node.next = curr.next # connect previous node to next node
        
        # make sure there is a next node
        if (curr.next != None):
            curr.next.prev = prev_node # connect next node to previous node


        return self.head
    
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # returns the length of the linked list
    def length(self):
        if self.head is None: # empty linked list
            return 0
        len = 0 # init length count
        curr = self.head # init current node
        while curr is not None:
            len += 1 # increment length
            curr = curr.next # update to next node
        return len
        
    # Time Complexity: O(n) - go through all elements
    # Space Complexity: O(n) - go through all elements
    # reverses the linked list iteratively, returns new head
    def reverseIterative(self):
        if self.head is None or self.head.next is None: # empty or 1 element
            return
        
        curr = self.head # create current node pointer
        prev = None # init previous ptr

        while curr is not None: # continue through end of linked list
            tmp = curr.next # store rest of linked list
            curr.next = prev # reverse ptr
            prev = curr # update prev node to current node
            curr = tmp # update current node to next node
        
        self.head = prev # update end node to be new head
        return self.head # return updated head



    # Time Complexity: O(n) - depends on llist size
    # Space Complexity: O(n) - depends on llist size
    # reverses the linked list recursively (Hint: you will need a helper function)
    def reverseRecursive(self):
        def reverse(head):
            # edge case check: empty linked list
            if head is None:
                return head
            # edge case check: one node linked list
            if head.next is None:
                return head

            # initialize new head and set recursive call
            new_head = reverse(head.next)

            # reverse pointer backwards
            head.next.next = head

            # remove old pointer to next node forwards
            head.next = None

            return new_head # return reversed list head
        
        # pass in head to recursive function
        self.head = reverse(self.head)



    # helper function to print out linked list
    def print_llist(self):
        if self.head is None:
            print("EMPTY LIST")
            return

        # store current node's next ptr
        curr = self.head
        while curr is not None:  # continue until end of linked list
            print(curr.val)  # print current node's value
            curr = curr.next  # move to next node


def main():
    # CREATE NODE AND LINKED LIST
    init_node = Node(1)
    llist = DoublyLinkedList(init_node)

    print("______ original list _____")
    llist.print_llist()
    assert llist.head is None

    # INSERT AT FRONT TEST CASES
    print("______insert 3 at front______")
    llist.insertAtFront(3)
    llist.print_llist()
    assert llist.head.val == 3

    print("______insert 2 at front______")
    llist.insertAtFront(2)
    llist.print_llist()
    assert llist.head.val == 2

    print("______insert 1 at front______")
    llist.insertAtFront(1)
    llist.print_llist()
    assert llist.head.val == 1

    # INSERT AT BACK TEST CASES
    print("______insert 4 at back______")
    llist.insertAtBack(4)
    llist.print_llist()
    assert llist.head.next.next.next.val == 4

    print("______insert 5 at back______")
    llist.insertAtBack(5)
    llist.print_llist()
    assert llist.head.next.next.next.next.val == 5

    print("______insert 6 at back______")
    llist.insertAtBack(6)
    llist.print_llist()
    assert llist.head.next.next.next.next.next.val == 6

    # INSERT AFTER TEST CASES
    print("______insert 0 after 2nd Node______")
    llist.insertAfter(0, llist.head.next)
    llist.print_llist()

    print("______insert 0 after 4th Node____")
    llist.insertAfter(0, llist.head.next.next.next)
    llist.print_llist()

    # DELETE FRONT TEST CASES
    print("______delete front value______")
    llist.deleteFront()
    llist.print_llist()

    print("______delete front value______")
    llist.deleteFront()
    llist.print_llist()


    print("______delete front value______")
    llist.deleteFront()
    llist.print_llist()


    print("______delete front value______")
    llist.deleteFront()
    llist.print_llist()

    # DELETE BACK TEST CASES
    print("______delete back value______")
    llist.deleteBack()
    llist.print_llist()

    print("______delete back value______")
    llist.deleteBack()
    llist.print_llist()

    # need more values
    llist.insertAtBack(1)
    llist.insertAtBack(2)
    llist.insertAtBack(3)
    llist.insertAtBack(4)
    print("___updated list____")
    llist.print_llist()

    # DELETE KTH NODE TEST CASES
    print("______delete 0th index value______")
    llist.deleteNode(0)
    llist.print_llist()

    print("______delete 3rd index value______")
    llist.deleteNode(3)
    llist.print_llist()

    # LLIST LENGTH TEST CASES
    print("______print linked list length______")
    llist.print_llist()

    # ITERATIVE REVERSE TEST CASES
    print("______print iterative reversed llist______")
    llist.reverseIterative()
    llist.print_llist()


# to make sure main is executed
if __name__ == '__main__':
    main()


