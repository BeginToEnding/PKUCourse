from Array import Array

class ArrayQueue():
    def __init__(self,capacity=10):
        self.__array = Array(capacity=capacity)
        self.dataname = 'ArrayQueue'
    
    def __str__(self):
        str_queue = 'ArrayQueue:size = %d , capacity = %d\n'%(self.__array.getSize(),self.__array.getCapcity())
        str_queue += 'front ['
        for i in range(self.__array.getSize()):
            str_queue += str(self.__array.get(i))
            if i != self.__array.getSize()-1:
                str_queue += ','
        str_queue += '] tail'
        return str_queue
    
    def isEmpty(self):
        return self.__array.isEmpty()
    
    def getSize(self):
        return self.__array.getSize()
    
    def getCapcity(self):
        return self.__array.getCapcity()
    
    def getData(self):
        return self.__array.getData()
    
    def getArray(self):
        return self.__array
    
    def enqueue(self, e):
        self.__array.addLast(e)
    
    def dequeue(self):
        return self.__array.removeFirst()
    
    def getFront(self):
        return self.__array.getFirst()
    

#时间复杂度为O(1)
class LoopQueue():
    def __init__(self,capacity=10):
        self.__data =  [None for i in range(capacity+1)]
        self.__capacity = capacity
        self.__front = 0
        self.__tail = 0
        self.__size = 0
        self.dataname = 'LoopQueue'
    
    def __str__(self):
        str_queue = 'LoopQueue:size = %d , capacity = %d\n'%(self.__size,self.__capacity)
        str_queue += 'front ['
        for i in range(self.__size):
            str_queue += str(self.__data[(i+self.__front)%len(self.__data)])
            if i != self.__size-1:
                str_queue += ','
        str_queue += '] tail'
        return str_queue
    
    def isEmpty(self):
        return self.__front == self.__tail
    
    def getSize(self):
        return self.__size
    
    def getCapcity(self):
        return self.__capacity
    
    def getData(self):
        return self.__data
    
    def enqueue(self, e):
        if (self.__tail+1) % len(self.__data) == self.__front:
            self.__resize(2*self.__capacity)
        self.__data[self.__tail] = e
        self.__tail = (self.__tail+1)%len(self.__data)
        self.__size += 1
    
    def __resize(self,newcapacity):
        self.__capacity = newcapacity
        new_data = [None for i in range(self.__capacity)]
        for i in range(self.__size):
            new_data[i] = self.__data[(i+self.__front)%len(self.__data)]
        self.__data = new_data
        self.__front = 0
        self.__tail = self.__size
    
    def dequeue(self):
        if self.isEmpty():
            raise Exception('Queue is empty')
        ret = self.__data[self.__front]
        self.__data[self.__front] = None
        self.__front = (self.__front+1)%len(self.__data)
        self.__size -= 1
        if self.__size == self.__capacity//4 and self.__capacity//2 != 0:
            self.__resize(self.__capacity//2)
        return ret
    
    def getFront(self):
        if self.isEmpty():
            raise Exception('Queue is empty')
        return self.__data[self.__front]
    

#双端队列
class Deque():
    def __init__(self,capacity=10):
        self.__data =  [None for i in range(capacity)]
        self.__capacity = capacity
        self.__front = 0
        self.__tail = 0
        self.__size = 0
        self.dataname = 'Deque'
    
    def __str__(self):
        str_queue = 'Deque:size = %d , capacity = %d\n'%(self.__size,self.__capacity)
        str_queue += 'front ['
        for i in range(self.__size):
            str_queue += str(self.__data[(i+self.__front)%len(self.__data)])
            if i != self.__size-1:
                str_queue += ','
        str_queue += '] tail'
        return str_queue
    
    def isEmpty(self):
        return self.__size == 0
    
    def getSize(self):
        return self.__size
    
    def getCapcity(self):
        return self.__capacity
    
    def getData(self):
        return self.__data
    
    def addFront(self, e):
        if self.__size == self.__capacity:
            self.__resize(2*self.__capacity)
        if self.__front == 0:
            self.__front = self.__capacity-1
        else:
            self.__front = self.__front-1
        self.__data[self.__front] = e
        self.__size += 1
    
    def addLast(self, e):
        if self.__size == self.__capacity:
            self.__resize(2*self.__capacity)
        self.__data[self.__tail] = e
        self.__tail = (self.__tail+1)%self.__capacity
        self.__size += 1

    def __resize(self,newcapacity):
        self.__capacity = newcapacity
        new_data = [None for i in range(self.__capacity)]
        for i in range(self.__size):
            new_data[i] = self.__data[(i+self.__front)%len(self.__data)]
        self.__data = new_data
        self.__front = 0
        self.__tail = self.__size
    
    def RemoveFront(self):
        if self.isEmpty():
            raise Exception('Queue is empty')
        ret = self.__data[self.__front]
        self.__data[self.__front] = None
        self.__front = (self.__front+1)%self.__capacity
        self.__size -= 1
        if self.__size == self.__capacity//4 and self.__capacity//2 != 0:
            self.__resize(self.__capacity//2)
        return ret
    
    def RemoveLast(self):
        if self.isEmpty():
            raise Exception('Queue is empty')
        if self.__tail == 0:
            self.__tail = self.__capacity-1
        else:
            self.__tail -= 1
        ret = self.__data[self.__tail]
        self.__data[self.__tail] = None
        self.__size -= 1
        if self.__size == self.__capacity//4 and self.__capacity//2 != 0:
            self.__resize(self.__capacity//2)
        return ret
    
    def getFront(self):
        if self.isEmpty():
            raise Exception('Queue is empty')
        return self.__data[self.__front]
    
    def getLast(self):
        if self.isEmpty():
            raise Exception('Queue is empty')
        if self.__tail == 0:
            return self.__data[self.__capacity-1]
        else:
            return self.__data[self.__tail-1]