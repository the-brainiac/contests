import math 
from collections import Counter, defaultdict
import sys, resource
# resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
# sys.setrecursionlimit(10**6)

"""
# Template Designed By: Shivshanker Singh
# Note: If you find this template useful and want to use it then please don't just copy paste it 
        you can take ideas from this and make your own.
        because if you copy paste as it is then there are high chances that both of us will be plagiarized
        (because most of code will be same for small problems).
        So to avoid this please dont copy paste.
"""

mod       = 10**9 + 7
input     = sys.stdin.readline
readInt   = lambda : int(input().strip())
readfloat = lambda : float(input().strip())
readStr   = lambda : input().strip()
intList   = lambda : list(map(int, input().strip().split()))
intMap    = lambda : map(int, input().strip().split())
floatList = lambda : list(map(float, input().strip().split()))
floatMap  = lambda : map(float, input().strip().split())
strList   = lambda : list(input().strip().split())


def print(*args, end='\n', sep=' '):
    for i in args:
        sys.stdout.write(str(i))
        sys.stdout.write(sep)
    sys.stdout.write(end)

N = 10**7 +1
is_prime = [1]*N
is_prime[0] = 0
is_prime[1] = 0

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
sieve()
res = [0]*(10**7+1)
for i in range(2, 10**7+1):
    res[i] = res[i-1]
    if is_prime[i]:
        res[i] += 1

# if __name__ == '__main__':
# for _ in range(readInt()):
#     n = readInt()
for n in range(2, 10**3 +1):
    print(res[n]-res[n//2]+1)
    
    