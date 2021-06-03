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
    ap, bh, n = intMap()
    power = intList()
    health = intList()
    d = dict()
    for i in range(n):
        d[power[i]] = health[i]
    power.sort(key=lambda x:(x,-d[x]))
    i = 0
    while i<n:
        if bh <= 0:
            break
        k = math.ceil(d[power[i]]/ap)
        if bh-(k-1)*power[i] <=0:
            bh -= k*power[i]
            break
        bh -= k*power[i]
        # d[power[i]] -= k*ap
        i += 1
        # print(d,bh)
    if bh > 0 or (i==n):
        print('YES')
    else:
        print('NO')