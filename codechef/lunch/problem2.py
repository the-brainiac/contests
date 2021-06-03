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
m = 10**9 + 7
if __name__ == "__main__":
    n = readInt()
    arr = intList()
    q = int(input())
    qrr = intList()
    res = sum(arr)
    for i in range(q):
        res = (res%m + res%m)%m
        print(res)
    
    # print('YES' if solve() else 'NO')