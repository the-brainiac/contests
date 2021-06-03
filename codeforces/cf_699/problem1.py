# import math 
from collections import Counter

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


for _ in range(readInt()):
    px, py = intMap()
    # arr = intList()
    s = input().strip()
    c = Counter(s)
    res = True
    if px >= 0:
        if c['R'] <px:
            res = False
    else:
        if c['L'] <abs(px):
            res = False
    if py >= 0:
        if c['U'] <py:
            res = False
    else:
        if c['D'] <abs(py):
            res = False
    if res:
        print('YES')
    else:
        print('NO')