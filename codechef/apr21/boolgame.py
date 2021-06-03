import math 
from collections import Counter, defaultdict

readInt   = lambda : int(input().strip())
readfloat = lambda : float(input().strip())
intList   = lambda : list(map(int, input().strip().split()))
intMap    = lambda : map(int, input().strip().split())
floatList = lambda : list(map(float, input().strip().split()))
floatMap  = lambda : map(float, input().strip().split())


def get_interval(s):
    interval = [False]*n
    start = 0
    
    for i in range(n):
        if s[i] == '1' and i !=0 and s[i-1]=='0':
            start = i
        if s[i] == '1':
            interval[i] = start
    
    # print(num, interval) 
    return interval
            
def get_score(num):
    score = 0 
    for i in range(n):
        if num[i] == '1':
            score += grr[i]
    
    mr_interval = get_interval(num)
    
    for u,v,d in mrr:
        if mr_interval[u-1] == mr_interval[v-1] and mr_interval[u-1]!=False:
            score += d
    
    return score
    
for _ in range(readInt()):
    # n = readInt()
    n, m, k = intMap()
    grr = intList()
    mrr = [intList() for i in range(m)]
    res = []
    
    for nm in range(2**n):
        num = bin(nm)[2:]
        num = '0'*(n-len(num)) + num
        res.append(get_score(num))
    # print(grr)
    print(*sorted(res, reverse=True)[:k])