import math 
from collections import Counter, defaultdict

readInt   = lambda : int(input().strip())
readfloat = lambda : float(input().strip())
intList   = lambda : list(map(int, input().strip().split()))
intMap    = lambda : map(int, input().strip().split())
floatList = lambda : list(map(float, input().strip().split()))
floatMap  = lambda : map(float, input().strip().split())


# N = 10**5
# is_prime = [1]*N
# is_prime[0] = 0
# is_prime[1] = 0

def sieve():
    i = 2
    while i*i <= N:
        if is_prime[i] == 0:
            i += 1
            continue

        j = 2*i
        while j < N:
            is_prime[j] = 0
            j += i

        i += 1
# sieve()

def solve(n, k):
    if k==0:
        return range(1,n+1)
    if k > (n-1)//2:
        return [-1]
    seg = range(1,n+1)
    start = 0
    end = n-1

    res = []
    
    res.append(seg[start])
    start += 1
    for i in range(k):
        if start >= end:
            break
        res.append(seg[end])
        end -= 1
        res.append(seg[start])
        start += 1
    for i in range(start,end+1):
        res.append(seg[i])

    return res

for _ in range(readInt()):
    # n = readInt()
    n, k = intMap()
    print(*solve(n, k))