# Question: PriorityQueue
# Time Spent: 40 min

# import statements
import heapq 

class PriorityQueue:
    def __init__(self, test_arr):
        heapq.heapify(test_arr) # use built-in heapify function instead
        self.test_arr = test_arr

    # priority queue front
    def top(self):
        return self.test_arr[0]

    # priority queue insertion
    def insert(self, val):
        heapq.heappush(self.test_arr, val)

    # remove from priority queue
    def remove(self):
        return heapq.heappop(self.test_arr)

    # print the priority queue
    def heap_print(self):
        print("PRINTING PRIORITY QUEUE: ", self.test_arr)


if __name__ == "__main__":

    # PRIORITY QUEUE TEST CASES
    test_list = [8, 5, 3, 4, 6, 2]
    # [2, 4, 3, 5, 6, 8, 7]
    # [3, 4, 7, 5, 6, 8]

    test_p_queue = PriorityQueue(test_list)

    # top of heap
    print("HEAP TOP: ", test_p_queue.top())
    test_p_queue.insert(7) # insert into heap
    test_p_queue.heap_print() # print heap
    test_p_queue.remove() # remove from heap
    test_p_queue.heap_print() # print heap one more time