"""
This is a user defined module for implementing Double Ended Priority
Queues (DEPQ) using a max and a min Heap data structure.

Author: Shravan
Date: 11-03-2024
"""
# importing MinHeap and MaxHeaps
from Heaps import MinHeap, MaxHeap

class DoubleEndedPriorityQueue:
    """Implementing Double Ended Priority Queue"""
    def __init__(self):
        self.min_heap = MinHeap()
        self.max_heap = MaxHeap()

    def size(self):
        return self.max_heap.size()

    def push(self, value):
        self.min_heap.push(value)
        self.max_heap.push(value)

    def removeMin(self):
        self.max_heap.pop()
        return self.min_heap.pop()

    def removeMax(self):
        self.min_heap.pop()
        return self.max_heap.pop()

    def getMin(self):
        return self.min_heap.getMin()

    def getMax(self):
        return self.max_heap.getMax()

    def isEmpty(self):
        return self.min_heap.isEmpty() and self.max_heap.isEmpty()

####-----Testing-------####
    
de_priority_queue = DoubleEndedPriorityQueue()
de_priority_queue.push(3)
de_priority_queue.push(1)
de_priority_queue.push(5)
de_priority_queue.push(6)
de_priority_queue.push(-1)
de_priority_queue.push(10)
print(de_priority_queue.isEmpty())
print("size: ", de_priority_queue.size())
print("Removing min: ", de_priority_queue.removeMin())
print("Removing min: ", de_priority_queue.removeMin())
print("Min Element:", de_priority_queue.getMin())

print("Removing max: ", de_priority_queue.removeMax())

print("Max Element:", de_priority_queue.getMax())
print("size: ", de_priority_queue.size())

### ----- output ---- ###
# False
# size:  6
# Removing min:  -1
# Removing min:  1
# Min Element: 3
# Removing max:  5
# Max Element: 3
# size:  3