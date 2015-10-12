from array_stack import ArrayStack
from my_exceptions import Empty
from music import *

# ETAOINH: A3 to G3
# S: REST
# R: Repeat
# The mappings dictionary we will be using
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

# Repeat character constant
repeat_char = 'r'


def __get_mapping(ch):
    # Convert to lower case so case is not significant 
    if mappings.has_key(ch.lower()):
        return mappings[ch.lower()]
    else:
        return None

def __append_repeat(notes, amount):
    '''
    Created to reduce code clutter, this simply returns the 
    associated key mapping value, or None if it does not exist
    '''
    # This makes sure we don't try to repeat more notes than actually exist
    to_use = amount if amount <= len(notes) else len(notes)
    # Checks if the amount of notes to copy is greater than 0, and then 
    # duplicates that amount at the end.
    if to_use > 0: notes += notes[-to_use:]

def text2notes (text):
    '''
    Takes text and maps it to notes.
    '''    
    notes = [] # The notes
    num_stack = ArrayStack() # Our stack of numbers
    
    for ch in text: # Iterate over every character in the string
        note = __get_mapping(ch) # Get the mapping
        if ch.isdigit(): 
            # If digit, add to num_stack
            num_stack.push(int(ch)) 
        elif ch.lower() == repeat_char and not num_stack.is_empty(): 
            # If the repeat character and numbers on the stack, 
            # pop the most recent number and call the repeat function 
            __append_repeat(notes, num_stack.pop())
        elif note != None:
            # If the note has a mapping, add it to notes
            notes.append(note)
    
    return notes
