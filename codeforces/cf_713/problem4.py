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
def solve(brr):
    brr.sort()
    arr_set = set(brr)
    s = sum(brr)
    flag = False
    c = Counter(brr)
    # print(s,brr)
    for i in range(n+1, -1, -1):
        if s-2*brr[i] in arr_set and ((s - 2*brr[i]) != brr[i] or c[brr[i]]>=2):
            bn1 = brr[i]
            bn2 = s - 2*brr[i]
            flag = True
            # print('helli')
            break
    
    if flag:
        c = Counter(brr)
        c[bn1] -= 1
        c[bn2] -= 1
        arr = []
        for i in c:
            for j in range(c[i]):
                arr.append(i)
        print(*arr)
    else:
        print(-1)

for _ in range(readInt()):
    n = readInt()
    brr = intList()
    solve(brr)