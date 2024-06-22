import time
from SelectionSort import SeclectionSort
from InsertionSort import InsertionSort
from MergeSort import MergeSort
from QuickSort import QuickSort
from Heap import HeapSort
from BubbleSort import BubbleSort
from ShellSort import ShellSort

class SortingHelper():
    def isSorted(arr):
        for i in range(1,len(arr)):
            if arr[i-1] > arr[i]:
                return False
        return True
    def sortTest(Sortname,arr):
        start = time.time()
        if Sortname == 'InsertionSort':
            InsertionSort.sort(arr,0,len(arr)-1)
        elif Sortname == 'SeclectionSort':
            SeclectionSort.sort(arr)
        elif Sortname == 'MergeSort':
            MergeSort.sort(arr,0,len(arr)-1)
        elif Sortname == 'MergeSort2':
            MergeSort.sort2(arr,0,len(arr)-1)
        elif Sortname == 'MergeSortBU':
            MergeSort.sortBU(arr)
        elif Sortname == 'MergeSortBU2':
            MergeSort.sortBU2(arr)    
        elif Sortname == 'QuickSort':
            QuickSort.sort(arr,0,len(arr)-1)
        elif Sortname == 'QuickSort2':
            QuickSort.sort2(arr,0,len(arr)-1)
        elif Sortname == 'QuickSort3':
            QuickSort.sort3(arr,0,len(arr)-1)
        elif Sortname == 'HeapSort':
            HeapSort.sort(arr)
        elif Sortname == 'HeapSort2':
            HeapSort.sort2(arr)
        elif Sortname == 'BubbleSort':
            BubbleSort.sort(arr)
        elif Sortname == 'ShellSort':
            ShellSort.sort(arr)
        elif Sortname == 'ShellSort2':
            ShellSort.sort2(arr)
        end = time.time()
        if not SortingHelper.isSorted(arr):
            raise RuntimeError(Sortname +' failed')
        print('%s, n = %d : %f s'%(Sortname,len(arr),end-start))