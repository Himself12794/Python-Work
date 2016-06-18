'''
Created on Oct 29, 2015

@author: Philip
'''
from queue import Empty

class LinkedStack:
    
    class _Node:
        
        __slots__ = '_element', '_next'
    
        def __init__(self, element, nexts):
            self._element = element
            self._next = nexts
            
    def __init__(self, params):
        
        self._head = None
        self._size = 0
        
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1
        
    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element
        
    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer
        
class _DoublyLinkedBase:
    
    class _Node:
        
        __slots__ = '_element', '_next', '_prev'
    
        def __init__(self, element, prev, nexts):
            self._element = element
            self._next = nexts
            self._prev = prev
            
    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0
        
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def _insert_between(self, e, predecessor, successor):
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest
    
    def _delete_node(self, node):
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element
         
    