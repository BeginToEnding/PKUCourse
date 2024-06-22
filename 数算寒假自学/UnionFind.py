#并查集呈现网络中节点间的连接状态
    
class UnionFind1():
    def __init__(self, size):
        self.__id = [i for i in range(size)]
    
    def getSize(self):
        return len(self.__id)
    
    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP == rootQ:
            return
        for i in range(len(self.__id)):
            if self.__id[i] == rootP:
                self.__id[i] = rootQ
    
    def find(self, p):
        if p < 0 or p >= len(self.__id):
            raise ValueError('p is out of bound.')
        return id[p]

    def isConnected(self, p, q):
        return self.find(p) == self.find(q)

class UnionFind2():
    def __init__(self, size):
        self.__parent = [i for i in range(size)]
    
    def getSize(self):
        return len(self.__parent)
    
    def union(self, p, q):    
        pRoot = self.find(p)
        qRoot = self.find(q)
        if pRoot == qRoot:
            return
        self.__parent[pRoot] = qRoot

    #时间复杂度为O(h)
    def find(self, p):
        if p < 0 or p >= len(self.__parent):
            raise Exception("p is out of bound.")
        while p != self.__parent[p]:
            p = self.__parent[p]
        return p

    def isConnected(self, p, q):
        return self.find(p) == self.find(q)
    
class UnionFind3():
    def __init__(self, size):
        self.__parent = [i for i in range(size)]
        self.__sz = [1]*size

    def getSize(self):
        return len(self.__parent)
    
    def union(self, p, q):    
        pRoot = self.find(p)
        qRoot = self.find(q)
        if pRoot == qRoot:
            return
        if self.__sz[pRoot] < self.__sz[qRoot]:
            self.__parent[pRoot] = qRoot
            self.__sz[qRoot] += self.__sz[pRoot]
        else:
            self.__parent[qRoot] = pRoot
            self.__sz[pRoot] += self.__sz[qRoot]
    
    #时间复杂度为O(h)
    def find(self, p):
        if p < 0 or p >= len(self.__parent):
            raise Exception("p is out of bound.")
        while p != self.__parent[p]:
            p = self.__parent[p]
        return p

    def isConnected(self, p, q):
        return self.find(p) == self.find(q)

class UnionFind4():
    def __init__(self, size):
        self.__parent = [i for i in range(size)]
        self.__rank = [1]*size
    
    def getSize(self):
        return len(self.__parent)
    
    def union(self, p, q):    
        pRoot = self.find(p)
        qRoot = self.find(q)
        if pRoot == qRoot:
            return
        if self.__rank[pRoot] < self.__rank[qRoot]:
            self.__parent[pRoot] = qRoot
        elif self.__rank[pRoot] > self.__rank[qRoot]:
            self.__parent[qRoot] = pRoot
        else:
            self.__parent[qRoot] = pRoot
            self.__rank[qRoot] += 1

    #时间复杂度为O(h)
    def find(self, p):
        if p < 0 or p >= len(self.__parent):
            raise Exception("p is out of bound.")
        while p != self.__parent[p]:
            p = self.__parent[p]
        return p
    
    def isConnected(self, p, q):
        return self.find(p) == self.find(q)

class UnionFind5():
    def __init__(self, size):
        self.__parent = [i for i in range(size)]
        self.__rank = [1]*size
    
    def getSize(self):
        return len(self.__parent)
    
    def union(self, p, q):    
        pRoot = self.find(p)
        qRoot = self.find(q)
        if pRoot == qRoot:
            return
        if self.__rank[pRoot] < self.__rank[qRoot]:
            self.__parent[pRoot] = qRoot
        elif self.__rank[pRoot] > self.__rank[qRoot]:
            self.__parent[qRoot] = pRoot
        else:
            self.__parent[qRoot] = pRoot
            self.__rank[qRoot] += 1

    #时间复杂度为O(h),添加路径压缩
    def find(self, p):
        if p < 0 or p >= len(self.__parent):
            raise Exception("p is out of bound.")
        while p != self.__parent[p]:
            self.__parent[p] = self.__parent[self.__parent[p]]
            p = self.__parent[p]
        return p
    
    def isConnected(self, p, q):
        return self.find(p) == self.find(q)

class UnionFind6():
    def __init__(self, size):
        self.__parent = [i for i in range(size)]
        self.__rank = [1]*size
    
    def getSize(self):
        return len(self.__parent)
    
    def union(self, p, q):    
        pRoot = self.find(p)
        qRoot = self.find(q)
        if pRoot == qRoot:
            return
        if self.__rank[pRoot] < self.__rank[qRoot]:
            self.__parent[pRoot] = qRoot
        elif self.__rank[pRoot] > self.__rank[qRoot]:
            self.__parent[qRoot] = pRoot
        else:
            self.__parent[qRoot] = pRoot
            self.__rank[qRoot] += 1
    
    #时间复杂度为O(h),递归添加路径压缩
    def find(self, p):
        if p < 0 or p >= len(self.__parent):
            raise Exception("p is out of bound.")
        while p != self.__parent[p]:
            self.__parent[p] = self.find[self.__parent[p]]
        return self.__parent[p]
    
    def isConnected(self, p, q):
        return self.find(p) == self.find(q)