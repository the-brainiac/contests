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
def getSum(n):
    res = 0
    while n:
        res += n%10
        n //= 10
    return res

def solve(n):
    while True:
        if math.gcd(n, getSum(n)) > 1:
            return n
        n += 1

for _ in range(readInt()):
    n = readInt()
    # a, b = intMap()
    # arr = intList()

    # print(a,b)
    print(solve(n))