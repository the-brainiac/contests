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
def solve(s, a, b):
    if a&1 and b&1:
        return -1
    start = 0
    end = len(s) -1
    while start <= end:
        if s[start] != s[end] and s[start] != '?' and s[end]!='?':
            return -1

        if s[start] != s[end]:
            if s[start] == '?':
                s[start] = s[end]
            else:
                s[end] = s[start]
        start += 1
        end -= 1
    c = Counter(s)
    if c['0'] > a or c['1'] > b:
        return -1
    a -= c['0']
    b -= c['1']

    start = 0
    end = len(s) -1
    while start <= end:
        if s[start] == '?' and s[end] == '?':
            if a > b:
                s[start] = '0'
                s[end] = '0'
                if start == end:
                    a -= 1
                else:
                    a -= 2
            else:
                s[start] = '1'
                s[end] = '1'
                if start == end:
                    b -= 1
                else:
                    b -= 2
        elif s[start] == '?' or s[end] == '?':
            if a > b:
                s[start] = '0'
                s[end] = '0'
                a -= 1
            else:
                s[start] = '1'
                s[end] = '1'
                b -= 1
                
        start += 1
        end -= 1
    # print(a,b)
    if a!= 0 or b!=0:
        return -1
    return ''.join(s)

for _ in range(readInt()):
    # n = readInt()
    a, b = intMap()
    s = list(input().strip())

    print(solve(s, a, b))