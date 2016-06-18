'''
Created on Oct 29, 2015

@author: Philip
'''

class PriorityQueueBase:
    '''Abstract base class for a priority queue.'''

    class _Item:
        '''Lightweight composite to store priority queue items.'''
        __slots__ = '_key', '_value'
        
        def __init__(self, k, v):
            self._key = k
            self._value = v
            
        def __lt__(self, other):
            return self._key < other._key
        
    def is_empty(self):
        '''Return True if the priority queue is empty'''
        return len(self) == 0
    
#class UnsortedPriorityQueue(PriorityQueueBase):
    #'''A min-oriented priority queue implemented with an unsorted list.'''
    
    #def _find_min(self):
    #    '''Return Position of item with minimum key.'''
    #    if self.is_empty():
    #        raise Empty('Priority queue is empty')
    #    small = self._data.first()
        
    #def __init__(self):
    #    self._data = PositionalList()'''