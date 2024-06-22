#用队列实现栈
from LinkedList import LinkedList

#push复杂度为O(1),pop复杂度为O(n)
class LinkedListStack():
    def __init__(self,capacity=10):
        self.__linkedlist = LinkedList()
        self.dataname = 'LinkedListStack'
    
    def __str__(self):
        str_stack = 'LinkedListStack:top '
        str_stack += str(self.__linkedlist)
        
        return str_stack
    
    def isEmpty(self):
        return self.__linkedlist.isEmpty()
    
    def getSize(self):
        return self.__linkedlist.getSize()
    
    def push(self, e):
        self.__linkedlist.addFirst(e)
    
    def pop(self):
        return self.__linkedlist.remove(0)
    
    def peek(self):
        return self.__linkedlist.getFirst()