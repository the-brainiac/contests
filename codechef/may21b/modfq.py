import math 
from collections import Counter, defaultdict
import sys
# sys.setrecursionlimit(10**6)

input     = sys.stdin.readline
readInt   = lambda : int(input().strip())
readfloat = lambda : float(input().strip())
readStr   = lambda : input().strip()
intList   = lambda : list(map(int, input().strip().split()))
intMap    = lambda : map(int, input().strip().split())
floatList = lambda : list(map(float, input().strip().split()))
floatMap  = lambda : map(float, input().strip().split())
strList   = lambda : list(input().strip().split())

"""
def print(*args):
	for i in args:
		sys.stdout.write(str(i))
		sys.stdout.write(' ')
	sys.stdout.write('\n')
"""

def solve(n, m):
    res = 0
    # sets greater than m
    if n>m:
        tn = n-m
        res += (tn*(tn+1))//2
    else:
        tn = 0
    res += (m-1)*tn
    last = min(n,m)
    for b in range(1,last+1):
        res += last//b -1
    return res

for _ in range(readInt()):
    n, m = intMap()
    
    print(solve(n, m))