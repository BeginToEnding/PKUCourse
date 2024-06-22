#用链表实现队列

#push复杂度为O(1),pop复杂度为O(n)
class LinkedListQueue():
    class Node():
        def __init__(self, e=None, next_node=None):
            self.e = e
            self.next = next_node
        
        def __str__(self):
            return str(self.e)
    
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0
        self.dataname = 'LinkedListQueue'
    
    def __str__(self):
        str_queue = 'LinkedListQueue:front '
        
        cur_node = self.__head
        while cur_node:
            str_queue += str(cur_node) + " -> "
            cur_node = cur_node.next
        str_queue += 'None tail'
        
        return str_queue
    
    def isEmpty(self):
        return self.__size == 0
    
    def getSize(self):
        return self.__size
    
    def enqueue(self, e):
        if self.__tail == None:
            self.__tail = self.Node(e)
            self.__head = self.__tail
        else:
            self.__tail.next = self.Node(e)
            self.__tail = self.__tail.next
        
        self.__size += 1

    def dequeue(self):
        if self.isEmpty():
            raise Exception('Cannot dequeue from an empty queue.')
        
        ret_node = self.__head
        self.__head = self.__head.next
        ret_node.next = None
        if self.__head == None:
            self.__tail = None
        
        self.__size -= 1
        
        return ret_node.e
    
    def getFront(self):
        if self.isEmpty():
            raise Exception('Queue is empty.')
        
        return self.__head.e