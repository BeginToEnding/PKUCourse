class Student():
    def __str__(self):
        return 'Student(name: %s , score: %d)'%(self.name,self.score)
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def checkclass(func):
        def inner(self,other):
            if self.__class__ != other.__class__:
                raise RuntimeError('Class is not equal')
            return func(self,other)
        return inner
    @checkclass
    def __eq__(self,other):
        return self.score == other.score
    @checkclass
    def __ne__(self,other):
        return self.score != other.score
    @checkclass
    def __gt__(self,other):
        return self.score > other.score
    @checkclass
    def __ge__(self,other):
        return self.score >= other.score
    @checkclass
    def __lt__(self,other):
        return self.score < other.score
    @checkclass
    def __le__(self,other):
        return self.score <= other.score
