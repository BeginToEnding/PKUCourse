from Array import Array

class ArrayStack():
    def __init__(self,capacity=10):
        self.__array = Array(capacity=capacity)
        self.dataname = 'ArrayStack'
    
    def __str__(self):
        str_stack = 'Stack:size = %d , capacity = %d\n'%(self.__array.getSize(),self.__array.getCapcity())
        str_stack += '['
        for i in range(self.__array.getSize()):
            str_stack += str(self.__array.get(i))
            if i != self.__array.getSize()-1:
                str_stack += ','
        str_stack += '] top'
        return str_stack
    
    def isEmpty(self):
        return self.__array.isEmpty()
    
    def getSize(self):
        return self.__array.getSize()
    
    def getCapcity(self):
        return self.__array.getCapcity()
    
    def getArray(self):
        return self.__array
    
    def push(self, e):
        self.__array.addLast(e)

    def pop(self):
        return self.__array.removeLast()
    
    def peek(self):
        return self.__array.getLast()