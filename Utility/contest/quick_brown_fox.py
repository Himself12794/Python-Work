from contest.secret_message import string_to_list

ALPHA = 'abcdefghijklmnopqrstuvwxyz'

def is_pangram(txt):
    has_chars = []
    
    for c in txt.lower():
        if not c in has_chars: has_chars.append(c)
        
    result = ''
    for c in ALPHA:
        if not c in has_chars: result += c
    
    return result

if __name__ == '__main__':
    print(is_pangram(ALPHA))
    print(is_pangram('I am insane'))
    