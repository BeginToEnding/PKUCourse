from copy import copy
class LinkedList():
    class Node():
        def __init__(self, e=None, next_node=None):
            self.e = e
            self.next = next_node
        
        def __str__(self):
            return str(self.e)
    
    def __init__(self):
        self.__dummyhead = self.Node(None,None)
        self.__size = 0
    
    def __str__(self):
        res = ''
        cur_node = self.__dummyhead.next
        while cur_node:
            res += str(cur_node) + " -> "
            cur_node = cur_node.next
        res += 'None'
        
        return res
    
    def getSize(self):
        return self.__size
    
    def isEmpty(self):
        return self.__size == 0
    
    def addFirst(self, e):
        self.add(0, e)
    
    def addLast(self, e):
        self.add(self.__size, e)
    
    def add(self, index, e):
        if index < 0 or index > self.__size:
            raise Exception('Add failed. Illegal index')
        prev_node = self.__dummyhead
        for i in range(index):
            prev_node = prev_node.next
        prev_node.next = self.Node(e,prev_node.next)
        
        self.__size += 1
    
    def get(self, index):
        if index < 0 or index > self.__size-1:
            raise Exception('Get failed. Illegal index')
        cur_node = self.__dummyhead.next
        for i in range(index):
            cur_node = cur_node.next
        return cur_node.e
    
    def getFirst(self):
        return self.get(0)
    
    def getLast(self):
        return self.get(self.__size-1)
    
    def set(self, index, e):
        if index < 0 or index > self.__size-1:
            raise Exception('Set failed. Illegal index')
        cur_node = self.__dummyhead.next
        for i in range(index):
            cur_node = cur_node.next
        cur_node.e = e
        
    def contains(self, e):
        cur_node = self.__dummyhead.next
        while cur_node:
            if cur_node.e == e:
                return True
            cur_node = cur_node.next
        
        return False
    
    def remove(self, index):
        if index < 0 or index > self.__size-1:
            raise Exception('Remove failed. Illegal index')
        prev_node = self.__dummyhead
        for i in range(index):
            prev_node = prev_node.next
        ret_node = prev_node.next
        prev_node.next = ret_node.next
        ret_node.next = None
        
        self.__size -= 1
        
        return ret_node.e
    
    def removeFirst(self):
        return self.remove(0)
    
    def removeLast(self):
        return self.remove(self.__size-1)
    
    def removeElements(self,e):
        prev_node = self.__dummyhead
        while prev_node.next:
            if prev_node.next.e == e:
                del_node = prev_node.next
                prev_node.next = del_node.next
                del_node.next = None
            else:
                prev_node = prev_node.next
        
        return self.__dummyhead.next
        
        
class LinkedListArr():
    def __init__(self, arr=None):
        if arr == None or len(arr) == 0:
            raise Exception('arr can not be empty')
        self.e = arr[0]
        self.next = None
        self.__size = len(arr)
        
        cur_node = self
        for i in range(1,len(arr)):
            cur_node.next = LinkedListArr([arr[i]])
            cur_node = cur_node.next
        
    def __str__(self):
        res = ''
        cur_node = self
        while cur_node:
            res += str(cur_node.e) + " -> "
            cur_node = cur_node.next
        res += 'None'
        
        return res
    
    def getSize(self):
        return self.__size
    
    def removeElementsRecur(self, e):
        if self == None:
            return None
        if self.next != None:
            self.next = self.next.removeElementsRecur(e)
        
        return self.next if self.e == e else self
    
    def Reverse(self):
        if self.__size == 1:
            return self
        prev_node = None
        cur_node = self
        
        while cur_node:
            next_node = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node
        
        return prev_node
    
    def ReverseR(self):
        if self == None or self.next == None:
            return self
        rev = self.next.ReverseR()
        self.next.next = self
        self.next = None
        
        return rev
        
class LinkedListR():
    class Node():
        def __init__(self, e=None, next_node=None):
            self.e = e
            self.next = next_node
        
        def __str__(self):
            return str(self.e)
    
    def __init__(self):
        self.__dummyhead = self.Node(None, None)
        self.__size = 0
    
    def __str__(self):
        res = ''
        cur_node = self.__dummyhead.next
        while cur_node:
            res += str(cur_node) + " -> "
            cur_node = cur_node.next
        res += 'None'
        
        return res
    
    def getSize(self):
        return self.__size
    
    def isEmpty(self):
        return self.__size == 0
    
    def addFirst(self, e):
        self.add(0, e)
    
    def addLast(self, e):
        self.add(self.__size, e)
    
    def add(self, index, e):
        if index < 0 or index > self.__size:
            raise Exception('Add failed. Illegal index')
        
        self.__dummyhead = self.__add(self.__dummyhead, index, e)
        self.__size += 1
    
    def __add(self, node, index, e):
        if index == 0:
            node.next = self.Node(e, node.next)
            return node
        node.next = self.__add(node.next, index-1, e)
        return node
    
    def get(self, index):
        if index < 0 or index > self.__size:
            raise Exception('Get failed. Illegal index')
        
        return self.__get(self.__dummyhead.next, index)
    
    def __get(self, node, index):
        if index == 0:
            return node.e
        return self.__get(node.next, index-1)
    
    def getFirst(self):
        return self.get(0)
    
    def getLast(self):
        return self.get(self.__size-1)
    
    def set(self, index, e):
        if index < 0 or index > self.__size-1:
            raise Exception('Set failed. Illegal index')
        
        self.__set(self.__dummyhead.next, index, e)

    def __set(self, node, index, e):
        if index == 0:
            node.e = e
            return
        self.__set(node.next, index-1, e)
        
    def contains(self, e):
        return self.__contains(self.__dummyhead.next, e)

    def __contains(self, node, e):
        if node == None:
            return False
        if node.e == e:
            return True
        return self.__contains(node.next, e)
        
    def remove(self, index):
        if index < 0 or index > self.__size-1:
            raise Exception('Remove failed. Illegal index')
        
        return self.__remove(self.__dummyhead, index)
    
    def __remove(self, node, index):
        if index == 0:
            ret_node = node.next
            node.next = ret_node.next
            ret_node.next = None
            return ret_node.e
        return self.__remove(node.next, index-1)
    
    def removeFirst(self):
        return self.remove(0)
    
    def removeLast(self):
        return self.remove(self.__size-1)
    
    def removeElements(self,e):
        self.__dummyhead.next = self.__removeElements(self.__dummyhead.next, e)

    def __removeElements(self, node, e):
        if node == None:
            return None
        node.next = self.__removeElements(node.next, e)
            
        return node.next if node.e == e else node