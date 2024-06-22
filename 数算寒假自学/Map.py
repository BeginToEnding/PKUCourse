from AVLTree import AVLTree

#时间复杂度为O(n)
class LinkedListMap():
    class Node():
        def __init__(self, key=None, value=None, next=None):
            self.key = key
            self.value = value
            self.next = next
        
        def __str__(self):
            return f"{self.key}: {self.value}"
    
    def __init__(self):
        self.__dummyhead = self.Node()
        self.__size = 0
    
    def getSize(self):
        return self.__size
    
    def isEmpty(self):
        return self.__size == 0
    
    def get(self, key):
        node = self.getNode(key)
        if node != None:
            return node.value
        return None 
    
    def getNode(self, key):
        cur = self.__dummyhead.next
        while cur != None:
            if cur.key == key:
                return cur
            cur = cur.next
        return None

    def contains(self, key):
        return self.getNode(key) != None
    
    def add(self, key, value):
        node = self.getNode(key)
        if node == None:
            self.__dummyhead.next = self.Node(key, value, self.__dummyhead.next)
            self.__size += 1
        else:
            node.value = value
    
    def set(self, key, value):
        node = self.getNode(key)
        if node != None:
            node.value = value
        else:
            raise KeyError("Key does not exist")
        
    def remove(self, key):
        prev = self.__dummyhead
        while prev.next != None:
            if prev.next.key == key:
                break
            prev = prev.next
        
        if prev.next != None:
            delNode = prev.next
            prev.next = delNode.next
            delNode.next = None
            self.__size -= 1
            return delNode.value
        
        return None

#时间复杂度为O(logn)
class BSTMap():
    class Node():
        def __init__(self, key=None, value=None, left=None, right=None):
            self.key = key
            self.value = value
            self.left = left
            self.right = right
        
        def __str__(self):
            return f"{self.key}: {self.value}"
    
    def __init__(self):
        self.__root = None
        self.__size = 0
        self.__keySet = []
    
    def getSize(self):
        return self.__size
    
    def isEmpty(self):
        return self.__size == 0
    
    def get(self, key):
        node = self.__getNode(self.__root, key)
        if node != None:
            return node.value
        return None
    
    def __getNode(self, node, key):
        if node ==None:
           return None
        if key == node.key:
           return node
        elif key < node.key:
           return self.__getNode(node.left, key)
        else:
           return self.__getNode(node.right, key)
    
    def add(self, key, value):
        self.__root = self.__add(self.__root, key, value)
        self.__keySet.append(key)

    def __add(self, node, key, value):
        if node == None:
            self.__size += 1
            return self.Node(key, value)
        if key < node.key:
            node.left = self.__add(node.left, key, value)
        elif key > node.key:
            node.right = self.__add(node.right, key, value)
        else:
            node.value = value

        return node
    
    def keySet(self):
        return self.__keySet
    
    def contains(self, key):
        return self.__getNode(self.__root, key) != None
    
    def set(self, key, value):
        node = self.__getNode(self.__root, key)
        if node != None:
            node.value = value
        else:
            raise KeyError("Key does not exist")
    
    def minimum(self):
        if self.__size == 0:
            raise Exception('Empty Tree')
        
        return self.__minimum(self.__root).key
    
    def __minimum(self, node):
        if node.left == None:
            return node
        return self.__minimum(node.left)
    
    def remove_min(self):
        ret = self.minimum()
        self.__root = self.__remove_min(self.__root)
        return ret
    
    def __remove_min(self, node):
        if node.left == None:
            rightNode = node.right
            node.right = None
            self.__size -= 1
            return rightNode
            
        node.left = self.__remove_min(node.left)
        return node
    
    def remove(self, key):
        node = self.__getNode(self.__root, key)
        if node != None:
            self.__root = self.__remove(self.__root, key)
            return node.value
        return None
    
    def __remove(self, node, key):
        if node == None:
            return None
        
        if key < node.key:
            node.left = self.__remove(node.left, key)
            return node
        elif key > node.key:
            node.right = self.__remove(node.right, key)
            return node
        else:
            if node.left == None:
                rightNode = node.right
                node.right = None
                self.__size -= 1
                retNode = rightNode
            elif node.right == None:
                leftNode = node.left
                node.left = None
                self.__size -= 1
                retNode = leftNode
            else:
                successor = self.Node(self.__minimum(node.right).key, self.__minimum(node.right).value)
                successor.right = self.__remove_min(node.right)
                #self.__size += 1
                successor.left = node.left
                node.left = None; node.right = None
                #self.__size -= 1
                retNode = successor
            
            return retNode

class AVLMap():    
    def __init__(self):
        self.__avl = AVLTree()
        self.__keySet = []
    
    def getSize(self):
        return self.__avl.getSize()
    
    def isEmpty(self):
        return self.__avl.isEmpty()
    
    def get(self, key):
        return self.__avl.get(key)
    
    def add(self, key, value):
        self.__avl.add(key, value)
        self.__keySet.append(key)
    
    def keySet(self):
        return self.__keySet
    
    def contains(self, key):
        return self.__avl.contains(key)
    
    def set(self, key, value):
        self.__avl.set(key, value)
    
    def remove(self, key):
        return self.__avl.remove(key)