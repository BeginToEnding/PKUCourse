#用队列实现栈
from Queue import ArrayQueue

#push复杂度为O(1),pop复杂度为O(n)
class QueueStack1():
    def __init__(self,capacity=10):
        self.__queue = ArrayQueue(capacity)
        self.__top = ''
        self.dataname = 'QueueStack1'
    
    def __str__(self):
        str_stack = 'QueueStack1:size = %d , capacity = %d\n'%(self.__queue.getSize(),self.__queue.getCapcity())
        str_stack += '['
        for i in range(self.__queue.getSize()):
            str_stack += str(self.__queue.getArray().get(i))
            if i != self.__queue.getSize()-1:
                str_stack += ','
        str_stack += '] top'
        return str_stack
    
    def isEmpty(self):
        return self.__queue.isEmpty()
    
    def getSize(self):
        return self.__queue.getSize()
    
    def getCapcity(self):
        return self.__queue.getCapcity()
    
    def push(self, e):
        self.__queue.enqueue(e)
        self.__top = e
    
    def pop(self):
        queue2 = ArrayQueue(self.__queue.getCapcity())
        while self.__queue.getSize()>1:
            self.__top = self.__queue.getFront()
            queue2.enqueue(self.__queue.dequeue())
        ret = self.__queue.dequeue() 
        self.__queue = queue2
        return ret
    
    def peek(self):
        return self.__top

#push复杂度为O(n),pop复杂度为O(1)
class QueueStack2():
    def __init__(self,capacity=10):
        self.__queue = ArrayQueue(capacity)
        self.dataname = 'QueueStack2'
    
    def __str__(self):
        str_stack = 'QueueStack2:size = %d , capacity = %d\n'%(self.__queue.getSize(),self.__queue.getCapcity())
        str_stack += '['
        for i in range(self.__queue.getSize()):
            str_stack += str(self.__queue.getArray().get(i))
            if i != self.__queue.getSize()-1:
                str_stack += ','
        str_stack += '] top'
        return str_stack
    
    def isEmpty(self):
        return self.__queue.isEmpty()
    
    def getSize(self):
        return self.__queue.getSize()
    
    def getCapcity(self):
        return self.__queue.getCapcity()
    
    def push(self, e):
        queue2 = ArrayQueue(self.__queue.getCapcity())
        while not self.isEmpty():
            queue2.enqueue(self.__queue.dequeue())
        self.__queue.enqueue(e)
        while not queue2.isEmpty():
            self.__queue.enqueue(queue2.dequeue())
    
    def pop(self):
        return self.__queue.dequeue()
    
    def peek(self):
        return self.__queue.getFront()

#只使用一个队列
class QueueStack3():
    def __init__(self,capacity=10):
        self.__queue = ArrayQueue(capacity)
        self.dataname = 'QueueStack3'
    
    def __str__(self):
        str_stack = 'QueueStack3:size = %d , capacity = %d\n'%(self.__queue.getSize(),self.__queue.getCapcity())
        str_stack += '['
        for i in range(self.__queue.getSize()):
            str_stack += str(self.__queue.getArray().get(i))
            if i != self.__queue.getSize()-1:
                str_stack += ','
        str_stack += '] top'
        return str_stack
    
    def isEmpty(self):
        return self.__queue.isEmpty()
    
    def getSize(self):
        return self.__queue.getSize()
    
    def getCapcity(self):
        return self.__queue.getCapcity()
    
    def push(self, e):
        self.__queue.enqueue(e)
        for _ in range(self.__queue.getSize()-1):
            self.__queue.enqueue(self.__queue.dequeue())
    
    def pop(self):
        return self.__queue.dequeue()
    
    def peek(self):
        return self.__queue.getFront()