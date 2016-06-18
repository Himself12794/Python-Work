'''
Created on Oct 29, 2015

@author: Philip
'''
from classwork.linkedlists import _DoublyLinkedBase

class PositionalList(_DoublyLinkedBase):

    class Position:
        
        def __init__(self, container, node):
            self._container = container
            self._node = node
            
        def element(self):
            return self._node._element
        
        def __eq__(self, other):
            return type( other ) is type( self ) and other._node is self._node
        
        def __ne__(self, other):
            return not (self == other)
        
    
    def _validate(self, p):
        
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._next is None:
            raise ValueError('p is no longer valid')
        return p._node
    
    def _make_position(self, node):
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)
        
    #---------------------------Accessors---------------------------------------
    def first(self):
        return self._make_position(self._header._next)
        