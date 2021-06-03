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
def get_len(n):
    res = 0 
    while n>0:
        n //= 10
        res += 1
    return res 

def solve(a, b, c):
    x = 10**(c-1)
    y = 10**(c-1)
    while True:
        if get_len(x) == a:
            break
        x *= 3
    while True:
        if get_len(y) == b:
            break
        y *= 7
    return x,y
    
for _ in range(readInt()):
    # n = readInt()
    a, b, c = intMap()
    # arr = intList()
    print(*solve(a,b,c))