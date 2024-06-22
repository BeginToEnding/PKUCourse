#用栈实现队列
from Stack import ArrayStack

#enqueue复杂度为O(1),dequeue复杂度为O(n)
class StackQueue1():
    def __init__(self,capacity=10):
        self.__stack = ArrayStack(capacity)
        self.dataname = 'StackQueue1'
        self.__top = ''
    
    def __str__(self):
        str_queue = 'StackQueue1:size = %d , capacity = %d\n'%(self.__stack.getSize(),self.__stack.getCapcity())
        str_queue += 'front ['
        for i in range(self.__stack.getSize()):
            str_queue += str(self.__stack.getArray().get(i))
            if i != self.__stack.getSize()-1:
                str_queue += ','
        str_queue += '] tail'
        return str_queue
    
    def isEmpty(self):
        return self.__stack.isEmpty()
    
    def getSize(self):
        return self.__stack.getSize()
    
    def getCapcity(self):
        return self.__stack.getCapcity()
    
    def enqueue(self, e):
        if self.__stack.isEmpty():
            self.__top = e
        self.__stack.push(e)

    def dequeue(self):
        stack2 = ArrayStack(self.__stack.getCapcity())
        while self.__stack.getSize()>1:
            self.__top = self.__stack.peek()
            stack2.push(self.__stack.pop())
        ret = self.__stack.pop() 
        while not stack2.isEmpty():
            self.__stack.push(stack2.pop())
        
        return ret
    
    def getFront(self):
        return self.__top

#enqueue复杂度为O(n),dequeue复杂度为O(1)
class StackQueue2():
    def __init__(self,capacity=10):
        self.__stack = ArrayStack(capacity)
        self.dataname = 'StackQueue2'
    
    def __str__(self):
        str_queue = 'StackQueue2:size = %d , capacity = %d\n'%(self.__stack.getSize(),self.__stack.getCapcity())
        str_queue += 'front ['
        for i in range(self.__stack.getSize()):
            str_queue += str(self.__stack.getArray().get(i))
            if i != self.__stack.getSize()-1:
                str_queue += ','
        str_queue += '] tail'
        return str_queue
    
    def isEmpty(self):
        return self.__stack.isEmpty()
    
    def getSize(self):
        return self.__stack.getSize()
    
    def getCapcity(self):
        return self.__stack.getCapcity()
    
    def enqueue(self, e):
        stack2 = ArrayStack(self.__stack.getCapcity())
        while not self.__stack.isEmpty():
            stack2.push(self.__stack.pop())
        self.__stack.push(e)
        while not stack2.isEmpty():
            self.__stack.push(stack2.pop())
    
    def dequeue(self):
        return self.__stack.pop()
    
    def getFront(self):
        return self.__stack.peek()

#enqueue复杂度为O(1),dequeue均摊复杂度为O(n)
class StackQueue3():
    def __init__(self,capacity=10):
        self.__stack1 = ArrayStack(capacity)
        self.__stack2 = ArrayStack(capacity)
        self.dataname = 'StackQueue3'
        self.__top = ''
    
    def __str__(self):
        str_queue = 'StackQueue3:size = %d , capacity = %d\n'%(
            self.__stack1.getSize()+self.__stack2.getSize(),
            self.__stack1.getCapcity()+self.__stack2.getCapcity())
        str_queue += 'front ['
        for i in range(0,self.__stack2.getSize()):
            str_queue += str(self.__stack2.getArray().get(self.__stack2.getSize()-i-1))
            if i != self.__stack2.getSize()-1:
                str_queue += ','
        if not self.__stack1.isEmpty() and not self.__stack2.isEmpty():
            str_queue += ','
        for i in range(self.__stack1.getSize()):
            str_queue += str(self.__stack1.getArray().get(i))
            if i != self.__stack1.getSize()-1:
                str_queue += ','
        str_queue += '] tail'
        return str_queue
    
    def isEmpty(self):
        return self.__stack1.isEmpty()&self.__stack2.isEmpty()
    
    def getSize(self):
        return self.__stack1.getSize()
    
    def getCapcity(self):
        return self.__stack1.getCapcity()
    
    def enqueue(self, e):
        if self.__stack1.isEmpty():
            self.__top = e
        self.__stack1.push(e)
    
    def dequeue(self):
        if not self.__stack2.isEmpty():
            return self.__stack2.pop()
        while self.__stack1.getSize()>1:
            self.__stack2.push(self.__stack1.pop())
        return self.__stack1.pop()
    
    def getFront(self):
        if not self.__stack2.isEmpty():
            return self.__stack2.peek()
        return self.__top