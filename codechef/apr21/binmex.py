import math 
from collections import Counter, defaultdict

readInt   = lambda : int(input().strip())
readfloat = lambda : float(input().strip())
intList   = lambda : list(map(int, input().strip().split()))
intMap    = lambda : map(int, input().strip().split())
floatList = lambda : list(map(float, input().strip().split()))
floatMap  = lambda : map(float, input().strip().split())


def check(num):
    b = bin(num)
    j = 2
    for i in string:
        if b[j] == i:
            j += 1
            
        if j == len(b): return False
        
    return True
    
def check_subsequence(s1, s2, l1, l2):
    if m == l1:
        return False
    if n == l2:
        return True
    global key
    if s1[l1] == s2[l2]:
        key = key[:l1+1]
        d[key] = d.get(key, check_subsequence(s1, s2, l1+1, l2+1))
        return d[key]
    
    d[key] = d.get(key, check_subsequence(s1, s2, l1, l2+1))
    return d[key]
    

for _ in range(readInt()):
    string = list(input())
    
    d = dict()
    num = 0
    n = len(string)
    while True:
        b = bin(num)[2:]
        global key
        key = b
        m = len(b)
        if check_subsequence(b, string, 0, 0):
            print(b)
            break
        num += 1