"""
This is a user defined module for implementing both varients
of the Heap data structure. We will implement Min and Max heap
in this module.

Author: Shravan
Date: 11-03-2024
"""

class MinHeap:
    """Class implementing MinHeap"""
    def __init__(self):
        self.heap = []

    def size(self):
        return len(self.heap)
    
    def isEmpty(self):
        return len(self.heap)==0
    
    def getMin(self):
        if not self.heap:
            raise IndexError("Heap is empty")
        return self.heap[0]

    def push(self, value):
        self.heap.append(value)
        self._heapify_up()

    def pop(self):
        if not self.heap:
            raise IndexError("Heap is empty")
        
        # Swap the root with the last element
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        popped_value = self.heap.pop()
        self._heapify_down()

        return popped_value

    def _heapify_up(self):
        index = len(self.heap) - 1
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] < self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def _heapify_down(self):
        index = 0
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            smallest = index

            if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[smallest]:
                smallest = left_child_index

            if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest]:
                smallest = right_child_index

            if smallest != index:
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
            else:
                break


#### ------------MAX - HEAP ----------------------- ####
            
class MaxHeap:
    """Class implementing MaxHeap"""
    def __init__(self):
        self.heap = []
    
    def size(self):
        return len(self.heap)
    
    def isEmpty(self):
        return len(self.heap)==0
    
    def getMax(self):
        if not self.heap:
            raise IndexError("Heap is empty")
        return self.heap[0]

    def push(self, value):
        self.heap.append(value)
        self._heapify_up()

    def pop(self):
        if not self.heap:
            raise IndexError("Heap is empty")
        
        # Swap the root with the last element
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        popped_value = self.heap.pop()
        self._heapify_down()

        return popped_value

    def _heapify_up(self):
        index = len(self.heap) - 1
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] > self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def _heapify_down(self):
        index = 0
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            largest = index

            if left_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[largest]:
                largest = left_child_index

            if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[largest]:
                largest = right_child_index

            if largest != index:
                self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
                index = largest
            else:
                break

