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

def solve(s):
    res = set()

    for i in range(1,n):
        if s[i] in res:
            return False
        if s[i] != s[i-1]:
            res.add(s[i-1])
    return True

for _ in range(readInt()):
    n = readInt()
    # a, b = intMap()
    s = input().strip()

    
    print('YES' if solve(s) else 'NO')