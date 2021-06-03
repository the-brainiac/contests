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

def solve(r, b, d):
    r, b = max(r, b), min(r, b)
    # print(r, b)
    if r==0 and b==0:
        return True
    if r-b<=d and b!= 0:
        return True
    if r == 0 or b==0:
        return False
    return solve(r-(1+d), b-1, d)

for _ in range(readInt()):
    # n = readInt()
    r, b, d = intMap()
    # arr = intList()
    print('YES' if solve(r, b, d) else 'NO')