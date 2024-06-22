#等长字符串排序算法Least Significant Digit
class LSDSort():
    sortname = 'LSDSort'
    @staticmethod
    def sort(arr, W):
        for s in arr:
            if len(s) != W:
                raise Exception(f"each string in arr must contain {W} digits")

        R = 256
        temp = arr*1
        for r in range(W-1, -1, -1): 
            cnt = [0]*R
            index = [0]*(R+1)
            for s in arr:
                cnt[ord(s[r])] += 1
            
            for i in range(R):
                index[i+1] = index[i] + cnt[i]
            
            for s in arr:
                temp[index[ord(s[r])]] = s
                index[ord(s[r])] += 1
            arr = temp*1
        return arr