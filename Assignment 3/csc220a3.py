from array_stack import ArrayStack
from my_exceptions import Empty
from music import *

# ETAOINH: A3 to G3
# S: REST
# R: Repeat
mappings = {
    "e":A3,
    "t":B3,
    "a":C3,
    "o":D3,
    "i":E3,
    "n":F3,
    "h":G3,
    "s":REST            
}

repeat_char = 'r'

def __get_mapping(ch):
    if mappings.has_key(ch.lower()):
        return mappings[ch.lower()]
    else:
        return None

def __append_repeat(notes, amount):
    to_use = amount if amount <= len(notes) else len(notes)
    if to_use > 0: notes += notes[-to_use:]

def text2notes (text):
    '''
    Takes text and maps it to notes.
    '''    
    notes = []
    num_stack = ArrayStack()
    
    for ch in text:
        note = __get_mapping(ch)
        if ch.isdigit():
            num_stack.push(int(ch)) 
        elif ch.lower() == repeat_char and not num_stack.is_empty():
            __append_repeat(notes, num_stack.pop())
        elif note != None:
            notes.append(note)
    
    return notes
