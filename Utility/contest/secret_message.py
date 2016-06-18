from math import sqrt, pow, ceil, floor

def next_perfect_square(num):
    sqr = sqrt(num)
    return num if sqr % 1 == 0 else pow(ceil(sqr), 2) 

def string_to_list(txt):
    return [c for c in txt]

def list_to_string(lst):
    txt = ''
    for c in lst: txt += c
        
    return txt

def encode(txt):
    sqr = int(next_perfect_square(len(txt)))
    root = int(floor(sqrt(sqr)))
    encoded = string_to_list(' ' * sqr)
    txt = string_to_list(txt)
    sqr -= 1
    
    for curr in range(sqr, 0, -1):
        encoded[(curr // root) + (root * (root - (curr % root) - 1))] = txt[sqr - curr] if sqr - curr < len(txt) else ' '
    
    return list_to_string(encoded).replace(' ', '')

if __name__ == '__main__':
    print(encode("IloveyoutooJill"))