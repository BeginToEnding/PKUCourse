#计算逆序对数，采用归并排序法的思路，复杂度为O(nlogn)
def ReversePairs(arr):
    def sort(arr, l, r, temp):
        res = 0
        if l < r:
            mid = l + (r-l)//2
            res += sort(arr, l, mid, temp)
            res += sort(arr, mid+1, r, temp)
            if arr[mid] > arr[mid+1]:
                res += merge(arr, l, mid, r, temp)
        return res
    
    def merge(arr, l, mid ,r, temp):
        temp[l:r+1] = arr[l:r+1]
        i = l; j = mid+1
        res = 0
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
                res += mid-i+1
        return res
    
    temp = arr*1
    return sort(arr, 0, len(arr)-1, temp)