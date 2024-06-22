from math import sqrt
from Merger import Merger

class SQRTDecomposition():
    def __init__(self, data, merger=Merger()):
        self.__N = len(data)
        self.__B = int(sqrt(self.__N))
        self.__Bn = self.__N // self.__B + (1 if self.__N % self.__B != 0 else 0)
        self.__data = data
        self.__merger = merger
        self.__blocks = [0]*self.__Bn
        for i in range(self.__N):
            if i % self.__B == 0:
                self.__blocks[i//self.__B] = self.__data[i]
            else:
                self.__merger.merge(self.__blocks[i//self.__B], self.__data[i])
    
    def queryRange(self, i, j):
        if i < 0 or j >= self.__N or i > j:
            raise Exception('Index is illegal.')
        res = self.__data[i]
        l = i // self.__B
        r = j // self.__B
        if l == r:
            for k in range(i+1, j+1):
                res = self.__merger.merge(res, self.__data[k])
        else:
            for k in range(i+1, self.__B*(l+1)):
                res = self.__merger.merge(res, self.__data[k])
            for k in range(l+1, r):
                res = self.__merger.merge(res, self.__blocks[k])
            for k in range(self.__B*r, j+1):
                res = self.__merger.merge(res, self.__data[k])
        return res
    
    def update(self, index, value):
        if index < 0 or index >= self.__N:
            raise Exception('Index is illegal.')
        
        b = index // self.__B
        self.__data[index] = value
        self.__blocks[b] = self.__data[b*self.__B]
        for i in range(b*self.__B+1, min((b+1)*self.__B, self.__N)):
            self.__blocks[b] = self.__merger.merge(self.__blocks[b], self.__data[i])