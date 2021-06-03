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
def check(s):
    d = defaultdict(list)
    for i in range(n):
        d[s[i]].append(i)
    tindex = sorted(d['T'])
    mindex = sorted(d['M'])
    mn = len(mindex)
    tn = len(tindex)
    if tn != 2*mn:
        return False

    for i in range(mn):
        if tindex[i] > mindex[i]:
            return False

    for i in range(mn):
        if tindex[mn+i] < mindex[i]:
            return False
    # print(d)
    return True


for _ in range(readInt()):
    n = readInt()
    # a, b = intMap()
    s = input().strip()
    print('YES' if check(s) else 'NO')