def isPalindrome (string):
    return [x.lower() for x in string if x.isalnum()] == [x.lower() for x in string if x.isalnum()][::-1]
