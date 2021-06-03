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
    s = input().strip()
    if set(s) == set('a'):
        print('NO')
    else:
        print('YES')
        start = 0
        end = len(s) -1
        while start <= end:
            if s[end]!='a':
                print(s[:start]+'a'+s[start:])
                break
            if s[start]!='a':
                print(s[:end]+'a'+s[end:])
                break
            start += 1
            end -= 1