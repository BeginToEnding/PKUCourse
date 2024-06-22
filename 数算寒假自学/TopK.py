from PriorityQueue import MaxPriorityQueue, MinPriorityQueue

#时间复杂度O(nlogk)，空间复杂度O(k)
def MinTopK(arr, k):
    pq = MaxPriorityQueue()
    res = []
    for i in range(k):
        pq.enqueue(arr[i])
    
    for i in range(k, len(arr)):
        if not pq.isEmpty() and arr[i] < pq.getFront():
            pq.dequeue()
            pq.enqueue(arr[i])

    for i in range(k):
        res.append(pq.dequeue())
    
    return res

def MaxTopK(arr, k):
    pq = MinPriorityQueue()
    res = []
    for i in range(k):
        pq.enqueue(arr[i])
    
    for i in range(k, len(arr)):
        if not pq.isEmpty() and arr[i] > pq.getFront():
            pq.dequeue()
            pq.enqueue(arr[i])

    for i in range(k):
        res.append(pq.dequeue())
    
    return res