#线段树是平衡二叉树，不一定是完全二叉树，解决区间查询问题
from Merger import Merger
from Queue import ArrayQueue

class SegmentTree():
    def __init__(self, arr=[], merger=Merger()):
        self.__merger = merger
        self.__data = arr*1
        self.__tree = [None]*(len(arr)*4)
        if len(arr) > 0:
            self.__buildSegmentTree(0, 0, len(arr)-1)
    
    def __str__(self):
        res = '['
        for i in range(len(self.__tree)):
            if res != None:
                res += str(self.__tree[i])
            else:
                res += 'None'
            if i != len(self.__tree)-1:
                res += ','
        res += ']'
        return res

    def getSize(self):
        return len(self.__data)
    
    def get(self, index):
        if index < 0 or index >= self.getSize():
            raise Exception('Index is illegal.')
        return self.__data[index]

    def leftChild(self, index):
        return 2*index + 1
    
    def rightChild(self, index):
        return 2*index + 2

    def __buildSegmentTree(self, treeIndex, l, r):
        if l == r:
            self.__tree[treeIndex] = self.__data[l]
            return
        leftTreeIndex = self.leftChild(treeIndex)
        rightTreeIndex = self.rightChild(treeIndex)
        mid = l + (r - l - 1) // 2
        self.__buildSegmentTree(leftTreeIndex, l, mid)
        self.__buildSegmentTree(rightTreeIndex, mid+1, r)
        self.__tree[treeIndex] = self.__merger.merge(self.__tree[leftTreeIndex], self.__tree[rightTreeIndex])
    
    def query(self, queryL, queryR):
        if queryL < 0 or queryL >= self.getSize() or queryR < 0 or queryR >= self.getSize() or queryL > queryR:
            raise Exception('Index is illegal.')
        return self.__query(0, 0, self.getSize()-1, queryL, queryR)
    
    def __query(self, treeIndex, l, r, queryL, queryR):
        if l == queryL and r == queryR:
            return self.__tree[treeIndex]
        mid = l + (r - l - 1) // 2
        leftTreeIndex = self.leftChild(treeIndex)
        rightTreeIndex = self.rightChild(treeIndex)
        if queryL >= mid+1:
            return self.__query(rightTreeIndex, mid+1, r, queryL, queryR)
        elif queryR <= mid:
            return self.__query(leftTreeIndex, l, mid, queryL, queryR)
        leftResult = self.__query(leftTreeIndex, l, mid, queryL, mid)
        rightResult = self.__query(rightTreeIndex, mid+1, r, mid+1, queryR)

        return self.__merger.merge(leftResult, rightResult)
    
    def update(self, index, e):
        if index < 0 or index >= self.getSize():
            raise Exception('Index is illegal.')
        self.__data[index] = e
        self.__update(0, 0, self.getSize()-1, index, e)
    
    def __update(self, treeIndex, l, r, index, e):
        if l == r:
            self.__tree[treeIndex] = e
            return
        mid = l + (r - l - 1) // 2
        leftTreeIndex = self.leftChild(treeIndex)
        rightTreeIndex = self.rightChild(treeIndex)
        if index >= mid+1:
            self.__update(rightTreeIndex, mid+1, r, index, e)
        else:
            self.__update(leftTreeIndex, l, mid, index, e)
        self.__tree[treeIndex] = self.__merger.merge(self.__tree[leftTreeIndex], self.__tree[rightTreeIndex])
        

class SegmentTree2():
    class Node():
        def __init__(self, e, l ,r):
            self.e = e
            self.l = l
            self.r = r
            self.left = None
            self.right = None
    
    def __init__(self, arr=[], merger=Merger()):
        self.__merger = merger
        self.__data = arr*1
        if len(arr) > 0:
            self.__root = self.__buildSegmentTree(0, len(arr)-1)
    
    def __str__(self):
        res = self.generate_str(self.__root,'')
        return res
    
    def generate_str(self, node, res, depth=0):
        if node == None:
            res += '--'*depth + 'None\n'
            return res
        res += '--'*depth + str(node.e) + '\n'
        res = self.generate_str(node.left, res, depth+1)
        res = self.generate_str(node.right, res, depth+1)
        return res
    
    def getSize(self):
        return len(self.__data)
    
    def __buildSegmentTree(self, l, r):
        if l == r:
            return self.Node(self.__data[l], l, r)
        mid = l + (r - l - 1) // 2
        leftNode = self.__buildSegmentTree(l, mid)
        rightNode = self.__buildSegmentTree(mid+1, r)
        node = self.Node(self.__merger.merge(leftNode.e, rightNode.e), l, r)
        node.left = leftNode
        node.right = rightNode
        return node
    
    def query(self, queryL, queryR):
        return self.__query(self.__root, queryL, queryR)
    
    def __query(self, node, queryL, queryR):
        if node.l == queryL and node.r == queryR:
            return node.e
        mid = node.l + (node.r - node.l - 1) // 2
        if queryL >= mid+1:
            return self.__query(node.right, queryL, queryR)
        elif queryR <= mid:
            return self.__query(node.left, queryL, queryR)
        return self.__merger.merge(self.__query(node.left, queryL, mid), self.__query(node.right, mid+1, queryR))
    
    def update(self, index, e):
        self.__data[index] = e
        self.__update(self.__root, index, e)

    def __update(self, node, index, e):
        if node.l == node.r:
            node.e = e
            return
        mid = node.l + (node.r - node.l - 1) // 2
        if index >= mid+1:
            self.__update(node.right, index, e)
        else:
            self.__update(node.left, index, e)
        node.e = self.__merger.merge(node.left.e, node.right.e)
    
    #前序遍历
    def pre_order(self):
        self.__pre_order(self.__root)
        
    def __pre_order(self, node):
        if node != None:
            print(node.e)
            self.__pre_order(node.left)
            self.__pre_order(node.right)
    
    #中序遍历
    def in_order(self):
        self.__in_order(self.__root)

    def __in_order(self, node):
        if node != None:
            self.__in_order(node.left)
            print(node.e)
            self.__in_order(node.right)
    
    #后序遍历
    def post_order(self):
        self.__post_order(self.__root)

    def __post_order(self, node):
        if node != None:
            self.__post_order(node.left)
            self.__post_order(node.right)
            print(node.e)

    def level_order(self):
        queue = ArrayQueue()
        queue.enqueue(self.__root)
        while not queue.isEmpty():
            node = queue.dequeue()
            print(node.e)
            if node.left != None:
                queue.enqueue(node.left)
            if node.right != None:
                queue.enqueue(node.right)
