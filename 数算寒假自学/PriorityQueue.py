from Heap import MaxHeap, MinHeap

class MaxPriorityQueue():
    def __init__(self):
        self.__maxHeap = MaxHeap()
    
    def getSize(self):
        return self.__maxHeap.getSize()

    def isEmpty(self):
        return self.__maxHeap.isEmpty()
    
    def getFront(self):
        return self.__maxHeap.findMax()
    
    def enqueue(self, e):
        self.__maxHeap.add(e)
    
    def dequeue(self):
        return self.__maxHeap.extractMax()
    
class MinPriorityQueue():
    def __init__(self):
        self.__minHeap = MinHeap()
    
    def getSize(self):
        return self.__minHeap.getSize()

    def isEmpty(self):
        return self.__minHeap.isEmpty()
    
    def getFront(self):
        return self.__minHeap.findMin()
    
    def enqueue(self, e):
        self.__minHeap.add(e)

    def dequeue(self):
        return self.__minHeap.extractMin()