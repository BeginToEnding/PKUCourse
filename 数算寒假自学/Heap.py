#二叉堆是完全二叉树
class MaxHeap():
    def __init__(self, arr=[]):
        self.data = arr[:]
        if len(arr) > 0:
            #时间复杂度为O(n)
            for i in range(self.parent(len(arr)-1), -1, -1):
                self.__shiftDown(i)
        
    def getSize(self):
        return len(self.data)
    
    def isEmpty(self):
        return len(self.data) == 0
    
    def parent(self, index):
        if index == 0:
            raise IndexError("index-0 doesn't have parent")
        return (index - 1) // 2
    
    def leftChild(self, index):
        return index * 2 + 1
    
    def rightChild(self, index):
        return index * 2 + 2
    
    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]
     
    def add(self, e):
        self.data.append(e)
        self.__shiftUp(self.getSize() - 1)

    def __shiftUp(self, index):
        while index > 0 and self.data[index] > self.data[self.parent(index)]:
            self.swap(index, self.parent(index))
            index = self.parent(index)

    def findMax(self):
        if self.isEmpty():
            raise ValueError("Can't find max when heap is empty")
        return self.data[0]
        
    def extractMax(self):
        ret = self.findMax()
        self.swap(0, self.getSize() - 1)
        self.data.pop()
        self.__shiftDown(0)
        return ret
    
    def __shiftDown(self, index):
        while self.leftChild(index) < self.getSize():
            j = self.leftChild(index)
            if j+1 < self.getSize():
                if self.data[j] < self.data[j+1]:
                    j = self.rightChild(index)
            if self.data[index] < self.data[j]:
                self.swap(index, j)
                index = j
            else:
                break
    
    def replace(self, e):
        ret = self.findMax()
        self.data[0] = e
        self.__shiftDown(0)
        return ret


class MinHeap():
    def __init__(self, arr=[]):
        self.data = arr[:]
        if len(arr) > 0:
            #时间复杂度为O(n)
            for i in range(self.parent(len(arr)-1), -1, -1):
                self.__shiftDown(i)
        
    def getSize(self):
        return len(self.data)
    
    def isEmpty(self):
        return len(self.data) == 0
    
    def parent(self, index):
        if index == 0:
            raise IndexError("index-0 doesn't have parent")
        return (index - 1) // 2
    
    def leftChild(self, index):
        return index * 2 + 1
    
    def rightChild(self, index):
        return index * 2 + 2
    
    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]
     
    def add(self, e):
        self.data.append(e)
        self.__shiftUp(self.getSize() - 1)
    
    def __shiftUp(self, index):
        while index > 0 and self.data[index] < self.data[self.parent(index)]:
            self.swap(index, self.parent(index))
            index = self.parent(index)
    
    def findMin(self):
        if self.isEmpty():
            raise ValueError("Can't find max when heap is empty")
        return self.data[0]
        
    def extractMin(self):
        ret = self.findMin()
        self.swap(0, self.getSize() - 1)
        self.data.pop()
        self.__shiftDown(0)
        return ret
    
    def __shiftDown(self, index):
        while self.leftChild(index) < self.getSize():
            j = self.leftChild(index)
            if j+1 < self.getSize():
                if self.data[j] > self.data[j+1]:
                    j = self.rightChild(index)
            if self.data[index] > self.data[j]:
                self.swap(index, j)
                index = j
            else:
                break
    
    def replace(self, e):
        ret = self.findMin()
        self.data[0] = e
        self.__shiftDown(0)
        return ret


class HeapSort():
    sortname = 'HeapSort'
    @staticmethod
    def sort(arr):
        h = MaxHeap()
        for i in arr:
            h.add(i)
        for i in range(len(arr)-1, -1, -1):
            arr[i] = h.extractMax()
    
    @staticmethod
    def sort2(arr):
        if len(arr) <= 1:
            return
        for i in range(len(arr)//2-1, -1, -1):
            HeapSort.__shiftDown(arr, i, len(arr))
        
        for i in range(len(arr)-1, -1, -1):
            arr[i], arr[0] = arr[0], arr[i]
            HeapSort.__shiftDown(arr, 0, i)
    
    @staticmethod
    def __shiftDown(arr, index, n):
        while 2*index+1 < n:
            j = 2*index+1
            if 2*index+2 < n:
                if arr[j] < arr[j+1]:
                    j = 2*index+2
            if arr[index] < arr[j]:
                arr[index], arr[j] = arr[j], arr[index]
                index = j
            else:
                break