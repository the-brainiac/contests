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
def solve(arr):
    s1 = s2 = 1
    seg1 = []
    seg2 = []
    for i in range(0,n,2):
        s1 &= arr[i]
        seg1.append(arr[i])
    for i in range(1,n,2):
        s2 &= arr[i]
        seg2.append(arr[i])
    res = 0
    if s1 != s2:
        return res
    c1 = Counter(seg1)
    c2 = Counter(seg2)
    for i in c1:
        if i in c2:
            res = (res%mod + (c1[i]*c2[i])%mod)%mod
    return res 

mod = 10**9 + 7

for _ in range(readInt()):
    n = readInt()
    # a, b = intMap()
    arr = intList()
    # print(a,b)
    print(solve(arr))