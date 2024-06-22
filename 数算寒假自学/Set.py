from BST import BST
from LinkedList import LinkedList
from AVLTree import AVLTree

class AVLSet():
    def __init__(self, items=None):
        self.__avl = AVLTree()
        if items != None:
            for item in items:
                self.add(item, None)
    
    def getSize(self):
        return self.__avl.getSize()
    
    def isEmpty(self):
        return self.__avl.isEmpty()
    
    def add(self, e):
        self.__avl.add(e, None)
    
    def remove(self, e):
        self.__avl.remove(e)

    def contains(self, e):
        return self.__avl.contains(e)
    
#时间复杂度为O(logn)
class BSTSet():
    def __init__(self, items=None):
        self.__bst = BST()
        if items != None:
            for item in items:
                self.add(item)
    
    def getSize(self):
        return self.__bst.getSize()
    
    def isEmpty(self):
        return self.__bst.isEmpty()
    
    def add(self, e):
        self.__bst.add(e)

    def remove(self, e):
        self.__bst.remove(e)

    def contains(self, e):
        return self.__bst.contains(e)

#时间复杂度为O(n)
class LinkedListSet():
    def __init__(self, items=None):
        self.__linkedlist = LinkedList()
        if items != None:
            for item in items:
                self.add(item)

    def getSize(self):
        return self.__linkedlist.getSize()
    
    def isEmpty(self):
        return self.__linkedlist.isEmpty()
    
    def add(self, e):
        if not self.__linkedlist.contains(e):
            self.__linkedlist.addFirst(e)

    def remove(self, e):
        self.__linkedlist.removeElements(e)

    def contains(self, e):
        return self.__linkedlist.contains(e)