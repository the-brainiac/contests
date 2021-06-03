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

def solve(arr, k):
    for i in range(n-1):
        if k==0:
            break
        opn = min(k, arr[i])
        arr[i] -= opn
        arr[-1] += opn
        k -= opn
    return arr

for _ in range(readInt()):
    # n = readInt()
    n, k = intMap()
    arr = intList()
    print(*solve(arr, k))
    # print('YES' if solve() else 'NO')