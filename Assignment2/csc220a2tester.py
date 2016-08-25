from csc220a2 import isPalindrome
from csc220a2testData import tests

def runTest ():
    score = 0
    n = len (tests)
    for (testId, string, expectedResult) in tests:
        try:
            result = isPalindrome (string)
            if result == expectedResult:
                print ('Test %d passed.' % testId)
                score = score + 1
            else:
                if expectedResult:
                    print ('Test %d failed: \'%s\' is a palindome, but your function reports it is not.' % (testId, string))
                else:
                    print ('Test %d failed: \'%s\' is not a palindome, but your function reports it is.' % (testId, string))
        except:
            print ('Test %d failed: unexpected exception.' % testId)

    testScore = min (max (15.0 * (score - n/2) * 2 / n, 0.0), 15.0)
    print ('\n%d of %d test cases passed. Score = %.2f of 15.00' % (score, n, testScore))

runTest ()
