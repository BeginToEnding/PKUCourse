#红黑树与2-3树等价，它们都满足二分搜索树的性质
#2-3树有两种节点：2节点存储一个元素，两个分叉；3节点存储两个元素，三个分叉
#2-3树是一种绝对平衡树，红黑树不是平衡树

#左倾红黑树
class RBTree():
    red = True
    black = False
    class Node():
        def __init__(self, key=None, value=None, left=None, right=None):
            self.key = key
            self.value = value
            self.left = left
            self.right = right
            self.color = RBTree.red
        
        def __str__(self):
            return f"{self.key}: {self.value}"
    
    def __init__(self):
        self.__root = None
        self.__size = 0
    
    def getSize(self):
        return self.__size
    
    def isEmpty(self):
        return self.__size == 0
    
    def isRed(self, node):
        if node == None:
            return RBTree.black
        return node.color == RBTree.red
    
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
    
    def rotateRight(self, node):
        newNode = node.left
        node.left = newNode.right
        newNode.right = node

        newNode.color = node.color
        node.color = RBTree.red
        
        return newNode
    
    def rotateLeft(self, node):
        newNode = node.right
        node.right = newNode.left
        newNode.left = node

        newNode.color = node.color
        node.color = RBTree.red
        
        return newNode
    
    def flipColors(self, node):
        node.color = RBTree.red
        node.left.color = RBTree.black
        node.right.color = RBTree.black
    
    def add(self, key, value):
        self.__root = self.__add(self.__root, key, value)
        self.__root.color = RBTree.black

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
        
        if self.isRed(node.right) and (not self.isRed(node.left)):
            node = self.rotateLeft(node)
        
        if (self.isRed(node.left)) and (self.isRed(node.left.left)):
            node = self.rotateRight(node)
        
        if (self.isRed(node.left)) and (self.isRed(node.right)):
            self.flipColors(node)
        
        return node
    
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