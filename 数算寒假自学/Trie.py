#字典树专门处理字符串
from Map import BSTMap


class Trie():
    class Node():
        def __init__(self, isEndOfWord=False):
            self.isEndOfWord = isEndOfWord
            self.next = BSTMap()
    
    def __init__(self):
        self.__root = self.Node()
        self.__size = 0
    
    def __str__(self):
        res = self.generate_str(self.__root,'')
        return res
    
    def generate_str(self, node, res, depth=1):
        if node.next.getSize() == 0:
            res += '--'*depth + 'None\n'
            return res
        
        for nextChar in node.next.keySet():
            res += '--'*depth + nextChar + '\n'
            res = self.generate_str(node.next.get(nextChar), res, depth+1)
        
        return res

    def getSize(self):
        return self.__size
    
    def add(self, word):
        self.__add(self.__root, 0, word)
    
    def __add(self, node, index, word):
        if index == len(word):
            if node.isEndOfWord != True:
                node.isEndOfWord = True
                self.__size += 1
                return
        c = word[index]
        if node.next.get(c) == None:
            node.next.add(c, self.Node())   
        self.__add(node.next.get(c), index + 1, word)
    
    def contains(self, word):
        return self.__contains(self.__root, 0, word)
    
    def __contains(self, node, index, word):
        if index == len(word):
            return node.isEndOfWord
        c = word[index]
        if node.next.get(c) == None:
            return False
        return self.__contains(node.next.get(c), index + 1, word)
    
    def isPrefix(self, prefix):
        return self.__isPrefix(self.__root, 0, prefix)
    
    def __isPrefix(self, node, index, prefix):
        if index == len(prefix):
            return True
        c = prefix[index]
        if node.next.get(c) == None:
            return False
        return self.__isPrefix(node.next.get(c), index + 1, prefix)
    
    def search(self, word):
        return self.__match(self.__root, 0, word)
    
    def __match(self, node, index, word):
        if index == len(word):
            return node.isEndOfWord
        c = word[index]
        if c != '.':
            if node.next.get(c) == None:
                return False
            return self.__match(node.next.get(c), index + 1, word)
        else:
            for nextChar in node.next.keySet():
                if self.__match(node.next.get(nextChar), index + 1, word):
                    return True
            return False
    
    def sum(self, prefix):
        cur = self.__root
        for i in range(len(prefix)):
            c = prefix[i]
            if cur.next.get(c) == None:
                return 0
            cur = cur.next.get(c)
        return self.__sum(cur)

    def __sum(self, node):
        res = int(node.isEndOfWord)
        if node.next.getSize() == 0:
            return res
        for nextChar in node.next.keySet():
            res += self.__sum(node.next.get(nextChar))
        return res
    
    def remove(self, word):
        self.__root = self.__remove(self.__root, 0, word)

    def __remove(self, node, index, word):
        if index == len(word):
            if node.isEndOfWord:
                node.isEndOfWord = False
                self.__size -= 1
                return None if node.next.getSize() == 0 else node
        c = word[index]
        if node.next.get(c) == None:
            return node
        if self.__remove(node.next.get(c), index + 1, word) == None:
            node.next.remove(c)
        
        return None if node.next.getSize() == 0 else node