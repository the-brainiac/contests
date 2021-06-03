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
def solve(s1, s2):
    d = defaultdict(set)
    # print(s1,s2)
    for i in range(len(s1)):
        for j in range(len(s1), i-1, -1):
            ts = s1[i:j]
            d[j-i].add(ts)
        for j in range(i):
            ts = s1[j:i]
            d[i-j].add(ts)
    # print(d)
    for i in sorted(d, reverse= True):
        for j in d[i]:
            if j in s2:
                n = len(j)
                return (len(s1)-n) + (len(s2)-n)
    return 0

for _ in range(readInt()):
    a = input().strip()
    b = input().strip()
    if len(a) < len(b):
        res = solve(a, b)
    else:
        res = solve(b, a)
    print(res)