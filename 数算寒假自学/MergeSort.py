#归并排序法，复杂度为O(nlogn)，空间复杂度为O(n)
from InsertionSort import InsertionSort

class MergeSort():
    sortname = 'MergeSort'
    #自顶向下的归并排序
    @staticmethod
    def sort(arr, l, r):
        if r - l <= 15:
            InsertionSort.sort(arr, l, r)
            return
        if l < r:
            mid = l + (r-l)//2
            MergeSort.sort(arr, l, mid)
            MergeSort.sort(arr, mid+1, r)
            if arr[mid] > arr[mid+1]:
                MergeSort.merge(arr, l, mid, r)
        
        return
    
    #节省内存，只创建一次temp
    @staticmethod
    def sort2(arr, l, r):
        temp = arr*1
        def sort2_inner(arr, l, r, temp):
            if r - l <= 15:
                InsertionSort.sort(arr, l, r)
                return
            if l < r:
                mid = l + (r-l)//2
                sort2_inner(arr, l, mid, temp)
                sort2_inner(arr, mid+1, r, temp)
                if arr[mid] > arr[mid+1]:
                    MergeSort.merge2(arr, l, mid, r, temp)
                return
        
        sort2_inner(arr, l, r, temp)
    
    #自底向上的归并排序
    @staticmethod
    def sortBU(arr):
        temp = arr*1
        n = len(arr)
        for sz in range(1, n):
            for i in range(0, n-sz, 2*sz):
                if arr[i+sz-1] > arr[i+sz]:
                    MergeSort.merge2(arr, i, i+sz-1, min(i+2*sz-1,n-1), temp)
    
    @staticmethod
    def sortBU2(arr):
        temp = arr*1
        n = len(arr)
        for i in range(0, n, 16):
            InsertionSort.sort(arr, i, min(i+15, n-1))
        for sz in range(16, n):
            for i in range(0, n-sz, 2*sz):
                if arr[i+sz-1] > arr[i+sz]:
                    MergeSort.merge2(arr, i, i+sz-1, min(i+2*sz-1,n-1), temp)
    
    @staticmethod
    def merge(arr, l, mid ,r):
        temp = arr[l:r+1]*1
        i = l; j = mid+1
        for k in range(l, r+1):
            if i > mid:
                arr[k] = temp[j-l]
                j += 1
            elif j > r:
                arr[k] = temp[i-l]
                i += 1
            elif temp[i-l] <= temp[j-l]:
                arr[k] = temp[i-l]
                i += 1
            else:
                arr[k] = temp[j-l]
                j += 1
    
    @staticmethod
    def merge2(arr, l, mid ,r, temp):
        temp[l:r+1] = arr[l:r+1]
        i = l; j = mid+1
        for k in range(l, r+1):
            if i > mid:
                arr[k] = temp[j]
                j += 1
            elif j > r:
                arr[k] = temp[i]
                i += 1
            elif temp[i] <= temp[j]:
                arr[k] = temp[i]
                i += 1
            else:
                arr[k] = temp[j]
                j += 1