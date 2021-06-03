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
    n1 = n//2
    if not n&1 and not n1&1:
        n2 = n1//2
        print(n1,n2,n2,end=' ')
    elif not n&1:
        n1 -= 1
        print(n1,n1,2,end=' ')
    else:
        print(n1,n1,1,end=' ')
    for i in range(k-3):
        print(1,end=' ')
    print()

for _ in range(readInt()):
    # n = readInt()
    n, k = intMap()
    # arr = intList()
    # print(a,b)
    solve(n-k+3,k)
    # print(arr)