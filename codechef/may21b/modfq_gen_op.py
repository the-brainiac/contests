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
    for i in range(1,n):
        for j in range(i+1, n+1):
            if (m%i)%j == (m%j)%i:
                print((i, j), end=' ')
                res += 1
        print()
    print(res) 
    return res
f = open('output.txt', 'w')
for _ in range(readInt()):
    n, m = intMap()
    
    f.write(str(solve(n, m))+'\n')
f.close()