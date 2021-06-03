import math 
from collections import Counter, defaultdict

readInt   = lambda : int(input().strip())
readfloat = lambda : float(input().strip())
intList   = lambda : list(map(int, input().strip().split()))
intMap    = lambda : map(int, input().strip().split())
floatList = lambda : list(map(float, input().strip().split()))
floatMap  = lambda : map(float, input().strip().split())




for _ in range(readInt()):
    n = readInt()
    arr = sorted(intList())
    brr = sorted(intList(), reverse=True)
    res = 0
    for i in range(n):
        res = max(res, arr[i]+brr[i])
    print(res)