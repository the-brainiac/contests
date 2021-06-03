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
	# n = readInt()
    # a, b = intMap()
    # arr = intList()
    s = input().strip()
    if sorted(s) == list(s):
        print('YES')
        continue
    prefix = True
    flag = True
    for i in range(len(s)-1):
        if s[i] == '1':
            prefix = False
        if s[i+1] == s[i] and s[i] == '0' and not prefix:
            flag = False
            break

    if flag:
        print('YES')
    else:
        print('NO')