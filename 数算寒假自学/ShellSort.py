#时间复杂度在O(n^2)与O(nlogn)之间
class ShellSort():
    sortname = 'ShellSort'
    @staticmethod
    def sort(arr):
        h = len(arr) // 2
        while h >= 1:
            for i in range(h, len(arr)):
                t = arr[i]; j = i
                while j >= h and t < arr[j-h]:
                    arr[j] = arr[j-h]
                    j -= h
                arr[j] = t
            
            h //= 2
        
    def sort2(arr):
        h = 1
        while h < len(arr) // 3:
            h = h * 3 + 1
        while h >= 1:
            for i in range(h, len(arr)):
                t = arr[i]; j = i
                while j >= h and t < arr[j-h]:
                    arr[j] = arr[j-h]
                    j -= h
                arr[j] = t
            h //= 3