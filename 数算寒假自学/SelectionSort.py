#每次找最小的,交换顺序，复杂度为O(n^2)
class SeclectionSort():
    sortname = 'SeclectionSort'
    @staticmethod
    def sort(arr):
        for i in range(len(arr)):
            if i < len(arr)-1:
                min_index = i
                for j in range(i+1,len(arr)):  
                    if arr[j] < arr[min_index]:
                        min_index = j
                SeclectionSort.Swap(arr,i,min_index)
            else:
                return arr
    @staticmethod
    def Swap(arr,i,j):
        t = arr[i]
        arr[i] = arr[j] 
        arr[j] = t

#print(SeclectionSort.sort([5,9,6,1,8,7]))
#SortingHelper.sortTest(SeclectionSort, ArrayGenerator.generateRandomArray(10000))