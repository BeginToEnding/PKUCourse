#字符串排序算法Most Significant Digit
class MSDSort():
    sortname = 'MSDSort'
    @staticmethod
    def sort(arr):
        MSDSort.__sort(arr, 0, len(arr)-1, 0)
        return
    
    @staticmethod
    def __sort(arr, left, right, r):
        if left >= right:
            return 
        R = 256
        temp = [0]*(right-left+1)
        cnt = [0]*(R+1)
        index = [0]*(R+2)
        
        for i in range(left, right+1):
            p = 0 if r>=len(arr[i]) else ord(arr[i][r])+1
            cnt[p] += 1
        
        for i in range(R+1):
            index[i+1] = index[i] + cnt[i]
        
        for i in range(left, right+1):
            p = 0 if r>=len(arr[i]) else ord(arr[i][r])+1
            temp[index[p]] = arr[i]
            index[p] += 1
        arr[left:right+1] = temp*1
        for i in range(R):
            MSDSort.__sort(arr, left+index[i], left+index[i+1]-1, r+1)
        

arr = ['ABC','BAC','CA','BAD','BD','BFE','CAB','CAD','CAE']
MSDSort.sort(arr)
print(arr)