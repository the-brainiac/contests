# import math 


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
    n, k = intMap()
    hrr = intList()
    while k>0:
        for i in range(n-1):
            if hrr[i]<hrr[i+1]:
                k -= 1
                hrr[i] += 1
                break
        if hrr == sorted(hrr,reverse=True):
            break
    if k>0:
        print(-1)
    else:
        print(i+1)