from QueueStack import QueueStack1,QueueStack2,QueueStack3
from StackQueue import StackQueue1,StackQueue2,StackQueue3
from Queue import ArrayQueue,LoopQueue,Deque
from LinkedList import LinkedList
from BST import BST
from Set import BSTSet, LinkedListSet
from SegmentTree import SegmentTree, SegmentTree2
from Merger import Merger
from Trie import Trie
from UnionFind import UnionFind6
from AVLTree import AVLTree
from RBTree import RBTree
from TestClass import Student
from DataHelper import DataHelper

'''
arrayStack = ArrayStack(5)
for i in range(5):
    arrayStack.push(i)
    print(arrayStack)
a = arrayStack.pop()
print(arrayStack)
print(a)
'''
'''
loopQueue = LoopQueue(5)
for i in range(5):
    loopQueue.enqueue(i)
    print(loopQueue)
loopQueue.dequeue()
print(loopQueue)
loopQueue.enqueue(11)
print(loopQueue)
loopQueue.enqueue(12)
print(loopQueue)
print(loopQueue.getFront())
'''
'''
arrayQueue = ArrayQueue(5)
loopQueue = LoopQueue(5)

DataHelper.dataTest(arrayQueue,10000)
DataHelper.dataTest(loopQueue,10000)
'''
'''
deque = Deque(5)
for i in range(16):
    if i%2==0:
        deque.addLast(i)
        print(deque)
    else:
        deque.addFront(i)
        print(deque)

for i in range(16):
    if i%2==0:
        deque.RemoveFront()
        print(deque)
    else:
        deque.RemoveLast()
        print(deque)
'''
'''
squeue1 = QueueStack1(10)
for i in range(5):
    squeue1.push(i)
    print(squeue1)
a = squeue1.pop()
print(squeue1)
print(a)
c = squeue1.peek()
print(c)

qsatck2 = QueueStack2(10)
for i in range(5):
    qsatck2.push(i)
    print(qsatck2)
a = qsatck2.pop()
print(qsatck2)
print(a)
c = qsatck2.peek()
print(c)

qsatck3 = QueueStack3(10)
for i in range(5):
    qsatck3.push(i)
    print(qsatck3)
a = qsatck3.pop()
print(qsatck3)
print(a)
c = qsatck3.peek()
print(c)
'''
'''
squeue1 = StackQueue1(10)
for i in range(5):
    squeue1.enqueue(i)
    print(squeue1)
a = squeue1.dequeue()
print(squeue1)
print(a)
c = squeue1.getFront()
print(c)

squeue2 = StackQueue2(10)
for i in range(5):
    squeue2.enqueue(i)
    print(squeue2)
a = squeue2.dequeue()
print(squeue2)
print(a)
c = squeue2.getFront()
print(c)

squeue3 = StackQueue3(10)
for i in range(5):
    squeue3.enqueue(i)
    print(squeue3)
squeue3.dequeue()
print(squeue3)
squeue3.enqueue(5)
print(squeue3)
c = squeue3.getFront()
print(c)
linkedlist = LinkedList()
for i in range(5):
    linkedlist.addFirst(i)
    print(linkedlist)

arr = [1,2,3,4,5,6]
st = SegmentTree2(arr)
print(st)
print(st.query(0,3))
st.update(1,8)
print(st)
print(st.query(0,3))
st.level_order()
'''
'''
trie = Trie()
trie.add('he')
trie.add('she')
trie.add('his')
trie.add('history')
print(trie.contains('his'))
trie.remove('his')
print(trie.contains('his'))
print(trie.contains('history'))
print(trie)
'''
rbt = RBTree()
arr = [5,7,3,4,2,6,8,1,9,5,9]
for i in arr:
    if rbt.contains(i):
        rbt.set(i, rbt.get(i) + 1)
    else:
        rbt.add(i, 1)
for i in arr:
    print(i, rbt.get(i), end='\n')
print(ord('a'))