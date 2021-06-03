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
def check(n, arr):
    for i in arr:
        val = math.sqrt(n*i)
        if val == int(val):
            return True
    return False

for _ in range(readInt()):
    # n = readInt()
    n, k = intMap()
    arr = intList()
    res = 0
    temp = arr.copy()
    val = 0
    while val < n-1:
        segment = []
        for i in range(val,n):
            if check(temp[i], segment):
                break
            else:
                segment.append(temp[i])
        val = i
        res += 1
        if val ==n-1:
            break
        print(segment,temp[val:])
    print(res)
    # print(arr)