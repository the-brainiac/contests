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
    c = Counter(arr)
    arr.sort(key= lambda x:(-c[x],x))
    mini = 10**10
    maxi = 0
    res = 0
    # print(arr)
    for i in range(n):
        mini = min(mini, arr[i])
        maxi = max(maxi, arr[i])
        res += maxi-mini
    return res
n = readInt()
arr = intList()
print(solve(arr))