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


for _ in range(readInt()):
    # n = readInt()
    n, k1, k2 = intMap()
    w, b = intMap()
    # arr = intList()
    k = min(k1,k2)
    w_cells = k + (k1-k)//2 + (k2-k)//2
    bk = n - max(k1, k2)
    b_cells = bk +(n-bk-k1)//2 + (n-bk-k2)//2
    if w_cells >=w and b_cells >= b:
        print('YES')
    else:
        print('NO')