#与前面的对象不断比较，对于有序数组，复杂度为O(n);一般来说，复杂度依然是O(n^2)
class InsertionSort():
    sortname = 'InsertionSort'
    @staticmethod
    def sort(arr, l, r):
        if l > r:
            raise Exception('Invalid parameters')
        for i in range(l+1, r+1):
            t = arr[i]
            for j in range(l, i):
                if t < arr[l+i-j-1]:
                    arr[l+i-j] = arr[l+i-j-1]
                    if j == i-1:
                        arr[l] = t
                else:
                    arr[l+i-j] = t 
                    break
        return