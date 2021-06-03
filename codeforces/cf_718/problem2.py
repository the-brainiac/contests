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

def solve():
    pass

for _ in range(readInt()):
    # n = readInt()
    n, m = intMap()
    brr = []
    for i in range(n):
        brr.append(sorted(intList()))
    
    dp = [[0]*m for i in range(n)]
    pat = [[0]*m for i in range(n)]

    top = [0 for i in range(n)]

    for i in range(m):
        mi = 10**10
        for j in range(n):
            if top[j] < m:
                if brr[j][top[j]] < mi:
                    mi = brr[j][top[j]]
                    idx = j
        dp[idx][i] = brr[idx][top[idx]]
        pat[idx][i] = 1
        top[idx] += 1

    for i in range(n):
        for j in range(m):
            if not pat[i][j]:
                dp[i][j] = brr[i][top[i]]
                top[i] += 1
            print(dp[i][j], end=" ")
        print()
        
    
    # print('YES' if solve() else 'NO')