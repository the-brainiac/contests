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

def solve(arr, x):
    if sum(arr)==x:
        print('NO')
        return
    print('YES')
    res = 0
    for i in range(n):
        if res + arr[i] == x:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            break
        res += arr[i]
    print(*arr)

for _ in range(readInt()):
    # n = readInt()
    n, x = intMap()
    arr = intList()
    
    solve(arr, x)
    # print('YES' if solve() else 'NO')
    