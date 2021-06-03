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
def solve(arr):
    server = [[0, 0], [0, 0]]
    idx = 0
    for i in arr:
        if (server[0][0] - server[0][1]) > (server[1][0] - server[1][1]):
            idx = 0
        else:
            idx = 1
        if i == 1:
            server[idx][0] += 1
        elif i == 2:
            server[idx][1] -= 1
        else:
            if server[idx][1] > server[idx][0]:
                server[idx][1] += 1
            else:
                server[idx][0] += 1

    return max(server[0][0], server[1][0])

for _ in range(readInt()):
    n = readInt()
    # a, b = intMap()
    arr = intList()
    print(solve(arr))
    # print(arr)