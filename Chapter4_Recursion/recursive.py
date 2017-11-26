def listsum(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + listsum(numList[1:])

print(listsum([1,3,5,7,9]))

def toStr(n, base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return toStr(n // base, base) + convertString[n % base]

print(toStr(1453, 16))

def reverseStr(string):
    if len(string) == 0:
        return ''
    elif len(string) == 1:
        return string[0]
    else:
        return string[-1] + reverseStr(string[:-1])

print(reverseStr(""))

def removeWhite(s):
    return ''.join(e for e in s if e.isalnum())

def helper(s1, s2):
    if s1 == s2:
        return True
    else:
        return False

def isPal(s):
    s = removeWhite(s)
    if len(s) <= 1:
        return True
    else:
        return helper(s[0], s[-1]) and isPal(s[1:-1])

print(isPal("madam i'm adam"))
print(isPal(""))
