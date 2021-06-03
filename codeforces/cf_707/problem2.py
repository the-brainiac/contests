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
    n = readInt()
    # a, b = intMap()
    arr = intList()
    res = ['0']*n
    i = n-1
    mn = n
    while i >= 0:
        temp = mn
        for j in range(min(i,temp),i-arr[i],-1):
            # print(j)
            if j>=0:
                res[j] = '1'
                mn = min(mn, j)
            else:
                break
        i -= 1

    print(' '.join(res))