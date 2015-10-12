'''
Created on Aug 20, 2015

@author: Philip
'''

class Fib:
    '''iterator that yields numbers in the Fibonacci sequence'''

    def __init__(self, maximum):
        self.max = maximum

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib
    
    def _toList(self):
        result = []
        for x in self:
            result.append(x)
        return result
    
    def __str__(self):
        return self.toList().__str__()
    
    def __getitem__(self, i):
        return self._toList()[i]
    
