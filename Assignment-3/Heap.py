# Question: Heap
# Time Spent: 40 min

# import statements
import heapq 

class Heap:
    def __init__(self, test_arr):
        heapq.heapify(test_arr) # use built-in heapify function instead
        self.test_arr = test_arr

    # heap top
    def top(self):
        return self.test_arr[0]

    # heap insertion
    def insert(self, val):
        heapq.heappush(self.test_arr, val)

    # remove from heap
    def remove(self):
        return heapq.heappop(self.test_arr)

    # print the heap
    def heap_print(self):
        print("PRINTING HEAP: ", self.test_arr)


if __name__ == "__main__":

    # HEAP TEST CASES
    test_list = [8, 5, 3, 4, 6, 2]
    # [2, 4, 3, 5, 6, 8, 7]
    # [3, 4, 7, 5, 6, 8]

    test_heap = Heap(test_list)

    # top of heap
    print("HEAP TOP: ", test_heap.top())
    test_heap.insert(7) # insert into heap
    test_heap.heap_print() # print heap
    test_heap.remove() # remove from heap
    test_heap.heap_print() # print heap one more time