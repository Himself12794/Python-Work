from data import tests
from csc220a3 import text2notes
from music import *

score = 0

def runTest (tc, intoput, output):
    try:
        notes = text2notes (intoput)
    except:
        print ('Test %d failed - exception caught.' % tc)
        return 0
    
    if len (notes) != len (output):
        print ('Test %d failed - expecting a note list of length %d, got %d instead.' % (tc, len (output), len (notes)))
        return 0

    n = len (output)
    for i in range (n):
        if notes [i] != output [i]:
            print ('Test %d failed - notes at position %d do not match.' % (tc, i))
            return 0

    print ('Test %d passed.' % tc)
    return 1

for (tc, intoput, output) in tests:
    score += runTest (tc, intoput, output)

print ('\n%d of 100 tests passed - score = %.2f of 15.00' % (score, score * 0.15))