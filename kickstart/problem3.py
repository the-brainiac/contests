import math 
from collections import Counter, defaultdict
import sys
sys.setrecursionlimit(10**6)

input     = sys.stdin.readline
readInt   = lambda : int(input().strip())
readfloat = lambda : float(input().strip())
readStr   = lambda : input().strip()
intList   = lambda : list(map(int, input().strip().split()))
intMap    = lambda : map(int, input().strip().split())
floatList = lambda : list(map(float, input().strip().split()))
floatMap  = lambda : map(float, input().strip().split())
strList   = lambda : list(input().strip().split())

"""
def print(*args):
    for i in args:
        sys.stdout.write(str(i))
        sys.stdout.write(' ')
    sys.stdout.write('\n')
"""
prime = []
primes = []
def simpleSieve(limit):
    
    mark = [True for i in range(limit + 1)]
    p = 2
    while (p * p <= limit):
        
        if (mark[p] == True):
            
            for i in range(p * p, limit + 1, p):
                mark[i] = False
        p += 1
        
    for p in range(2, limit):
        if mark[p]:
            prime.append(p)
            primes.append(p)
            # print(p,end = " ")
            
def segmentedSieve(n):
    
    limit = int(math.floor(math.sqrt(n)) + 1)
    simpleSieve(limit)
    
    low = limit
    high = limit * 2
    
    while low < n:
        if high >= n:
            high = n
            
        mark = [True for i in range(limit + 1)]
        
        for i in range(len(prime)):
            
            loLim = int(math.floor(low / prime[i]) *
                                        prime[i])
            if loLim < low:
                loLim += prime[i]
                
            for j in range(loLim, high, prime[i]):
                mark[j - low] = False
                
        for i in range(low, high):
            if mark[i - low]:
                primes.append(i)
                # print(i, end = " ")
                
        low = low + limit
        high = high + limit


segmentedSieve(10**8)
# print(len(primes), len(prime))
def solve(z):
    res = 6
    prev = 3
    for i in range(2,len(primes)):
        temp = primes[i-1] * primes[i]
        if temp > z:
            return res
        res = temp

for _ in range(readInt()):
    z = readInt()
    print(f'Case #{_+1}: ',end='')
    print(solve(z))