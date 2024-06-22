#import sys
#sys.setrecursionlimit(10000)
import random

class QuickSort():
    sortname = 'QuickSort'
    @staticmethod
    def sort(arr, l, r):
        if l >= r:
            return
        p = QuickSort.partition(arr, l, r)
        QuickSort.sort(arr, l, p-1)
        QuickSort.sort(arr, p+1, r)
    
    #双路快速排序
    @staticmethod
    def sort2(arr, l, r):
        if l >= r:
            return
        p = QuickSort.partition2(arr, l, r)
        QuickSort.sort2(arr, l, p-1)
        QuickSort.sort2(arr, p+1, r)
    
    #三路快速排序，解决相同值过多的情况
    @staticmethod
    def sort3(arr, l, r):
        if l >= r:
            return
        lt, gt = QuickSort.partition3(arr, l, r)
        QuickSort.sort3(arr, l, lt-1)
        QuickSort.sort3(arr, gt, r)
    
    @staticmethod
    def partition(arr, l, r):
        m = l + random.randint(0, r-l)
        arr[l], arr[m] = arr[m], arr[l]
        j = l
        for i in range(l+1, r+1):
            if arr[i] < arr[l]:
                j += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[l], arr[j] = arr[j], arr[l]
        return j
        
    @staticmethod
    def partition2(arr, l, r):
        m = l + random.randint(0, r-l)
        arr[l], arr[m] = arr[m], arr[l]
        i = l+1; j = r
        while True:
            while i <= j and arr[j] > arr[l]:
                j -= 1
            while i <= j and arr[i] < arr[l]:
                i += 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1; j -= 1
            else:
                break
        arr[l], arr[j] = arr[j], arr[l]
        return j
    
    @staticmethod
    def partition3(arr, l, r):
        m = l + random.randint(0, r-l)
        arr[l], arr[m] = arr[m], arr[l]
        lt = l; i = l+1; gt = r+1
        while i < gt:
            if arr[i] < arr[l]:
                lt += 1
                arr[i], arr[lt] = arr[lt], arr[i]
                i += 1
            elif arr[i] > arr[l]:
                gt -= 1
                arr[i], arr[gt] = arr[gt], arr[i]
            else:
                i += 1
        arr[l], arr[lt] = arr[lt], arr[l]
        #arr[l, lt-1] < v, arr[lt, i-1] == v, arr[gt, r] > v
        return lt, gt