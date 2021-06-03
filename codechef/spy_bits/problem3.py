import math 
from collections import Counter, defaultdict

readInt   = lambda : int(input().strip())
readfloat = lambda : float(input().strip())
intList   = lambda : list(map(int, input().strip().split()))
intMap    = lambda : map(int, input().strip().split())
floatList = lambda : list(map(float, input().strip().split()))
floatMap  = lambda : map(float, input().strip().split())

# f = open('output.txt', 'w')

n = readInt()
arr = intList()
q = readInt()
zero_set =  set()
for _ in range(q):
    res = 0
    x, k = intMap()
    idx = x-1
    flag = False
    while idx < n and k > 0:
        if len(zero_set) == n:
            print('0\n'*(q-_))
            flag = True
            break
        p = min(k, arr[idx])
        k -= p
        arr[idx] -= p
        if arr[idx] == 0:
            zero_set.add(idx)
        res += p*(idx+1-x)
        idx += 1
    if flag:
        break
    print(res)
# f.close()