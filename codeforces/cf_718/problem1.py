import math 
from collections import Counter, defaultdict
import sys
# sys.setrecursionlimit(10**6)

# input     = sys.stdin.readline
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

def solve(n):
    if n<2050 or n%2050 !=0:
        return -1
    res = n//2050
    total = 0
    while res > 0:
        total += res%10
        res //= 10
    return total 
for _ in range(readInt()):
    n = readInt()
    
    print(solve(n))