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
def seg(arr):
    if len(arr) ==0:
        return 0
    val = arr[0]
    count = 1
    for i in arr:
        if i != val:
            count += 1
            val = i
    return count

    
n = readInt()
arr = intList()
a0 = [arr[0]]
a1 = []
for i in range(1,n):
    if a0[-1]==arr[i]:
        a1.append(arr[i])
    else:
        a0.append(arr[i])
# print(a0,a1)
print(len(a0)+seg(a1))