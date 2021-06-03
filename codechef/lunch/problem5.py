import math 
from collections import Counter, defaultdict
import sys
from itertools import combinations
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

def solve():
    pass
m = 10**9 + 7
for _ in range(readInt()):
    # n = readInt()
    n, m, b = intMap()
    arr = [intList() for i in range(n)]
    r = []
    c = []
    for l in range(1, n+1):
        r += list(combinations(range(n),l))
    for l in range(1, m+1):
        c += list(combinations(range(m),l))
    res = 0
    # print(r)
    # print(c)
    for rows in r:
        for cols in c:
            temp = 0
            for i in rows:
                for j in cols:
                    temp += arr[i][j]
            if temp == b:
                res += 1
                
    print(res)
    # print('YES' if solve() else 'NO')