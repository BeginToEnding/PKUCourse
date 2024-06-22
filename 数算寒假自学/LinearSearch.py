import time
from ArrayGenerator import ArrayGenerator
from TestClass import Student

class LinearSearch(object):
    def __new__(cls, *args, **kwargs):
        raise TypeError("该类不能实例化")
    @staticmethod
    def Search(data, target):
        for i in range(len(data)):
            if data[i]==target:
                return i
            else:
                continue
        return "No target was found!"

    @staticmethod
    def time():
        datasize = [100000,1000000]
        for n in datasize:
            array = ArrayGenerator.generateOrderedArray(n)
            start = time.time()
            for i in range(100):
                LinearSearch.Search(array,n)
            end = time.time()
            print('n =',n,', 100 runs:',(end-start)/100,'s')

A = Student('A',90)
B = Student('B',80)
print(LinearSearch.Search([Student('A',85),Student('B',70),Student('C',80)],B))
LinearSearch.time()