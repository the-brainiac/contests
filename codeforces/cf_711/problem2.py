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

def check(c):
    for i in c:
        if c[i] > 0:
            return True
    return False

def solve(arr, w):
    c = Counter(arr)
    # arr.sort(reverse=True)
    res = 0
    while check(c):
        th = w
        for i in sorted(c, reverse=True):
            if th <=0:
                break
            if th >= i and c[i] > 0:
                p = th//i
                b = min(p, c[i])
                c[i] -= b
                th -= i*b
        res += 1
        # print(c)
    return res


for _ in range(readInt()):
	# n = readInt()
    n, w = intMap()
    arr = intList()
    print(solve(arr, w))