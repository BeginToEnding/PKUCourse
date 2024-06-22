import random


# 时间复杂度为O(n)，空间复杂度为O(1)
def SelectK(arr, l, r, k):
    def partition(arr, l, r):
        m = l + random.randint(0, r - l)
        arr[l], arr[m] = arr[m], arr[l]
        i = l + 1;
        j = r
        while True:
            while i <= j and arr[j] > arr[l]:
                j -= 1
            while i <= j and arr[i] < arr[l]:
                i += 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1;
                j -= 1
            else:
                break
        arr[l], arr[j] = arr[j], arr[l]
        return j

    p = partition(arr, l, r)
    if k - 1 == p:
        return arr[p]
    elif k - 1 < p:
        return SelectK(arr, l, p - 1, k)
    else:
        return SelectK(arr, p + 1, r, k)


def SelectKR(arr, l, r, k):
    def partition(arr, l, r):
        m = l + random.randint(0, r - l)
        arr[l], arr[m] = arr[m], arr[l]
        x = arr[l]
        i = l + 1;
        j = r
        while True:
            while i <= j and arr[i] < x:
                i += 1
            while i <= j and arr[j] > x:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1;
                j -= 1
            else:
                break
        arr[l], arr[j] = arr[j], arr[l]
        return j

    while l <= r:
        p = partition(arr, l, r)
        if p == k - 1:
            return arr[p]
        elif p > k - 1:
            r = p - 1
        else:
            l = p + 1
