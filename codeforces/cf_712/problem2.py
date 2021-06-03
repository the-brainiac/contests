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
def check(s1,s2):
    zo_count = [False]*n
    z_count = 0
    o_count = 0
    for i in range(n):
        if s1[i] == '0':
            z_count += 1
        else:
            o_count += 1
        if z_count == o_count:
            zo_count[i] = True
    flip = 0
    # print(zo_count)
    for i in range(n-1,-1,-1):
        if flip == 0:
            if s1[i] != s2[i]:
                if zo_count[i] == False:
                    return False
                flip = 1
        else:
            if s1[i] == s2[i]:
                if zo_count[i] == False:
                    return False
                flip = 0
        # print(s1[i],s2[i],flip)
            
    return True

for _ in range(readInt()):
    n = readInt()
    s1 = input().strip()
    s2 = input().strip()
    if check(s1,s2):
        print('YES')
    else:
        print('NO')