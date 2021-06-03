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
    n = readInt()
    # a, b = intMap()
    arr = [list(input().strip()) for i in range(n)]
    # print(a,b)
    idx = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == '*':
                idx.append((i, j))
        if len(idx) ==2:
            break
    # print(idx)
    
    x1, y1 = idx[0]
    x2, y2 = idx[1]
    if x1 == x2:
        arr[(x1+1)%n][y1] = '*'
        arr[(x2+1)%n][y2] = '*'
    elif y1 == y2:
        arr[x1][(y1+1)%n] = '*'
        arr[x2][(y2+1)%n] = '*'
    else:
        arr[x2][y1] = '*'
        arr[x1][y2] = '*'
    for i in arr:
        print(''.join(i))
    # print()