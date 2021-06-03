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
def solve(s, n, k):
    res = 0
    start = -1
    end = -1
    for i in range(n):
        if s[i] == '*':
            start = i
            break
    
    for i in range(n-1, -1, -1):
        if s[i] == '*':
            end = i
            break
    if start == end:
        return 1
    if end - start <=k:
        return 2
    res = 2
    while start +k < end:
        # print(start, end, '$$$$$')
        for i in range(start+k, start, -1):
            if s[i] == '*':
                start = i
                res += 1
                break

    return res

for _ in range(readInt()):
	# n = readInt()
    n, k = intMap()
    # arr = intList()
    s = input().strip()
    res = solve(s, n, k)

    print(res)
    # print(arr)