import math 
from collections import Counter, defaultdict
import sys
sys.setrecursionlimit(10**6)

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

def solve(arr):
    res = set()
    new_arr = []
    for i in range(1,n):
        new_arr.append(arr[i]-arr[i-1])
    # print(arr)
    # print(new_arr)
    if n==2 or len(set(new_arr))==1 or len(set(new_arr))==2:
        return n
    d = defaultdict(list)
    c = 1
    start = 0
    for i in range(1,n-1):
        if new_arr[i] == new_arr[i-1]:
            c += 1
        else:
            d[new_arr[i-1]].append([start, i-1])
            c = 1
            start = i
    d[new_arr[i]].append([start, i])
    for key in d:
        i = d[key]
        il = len(i)
        i.sort()
        res.add(i[0][1]-i[0][0]+2)
        for j in range(1,il):
            if i[j][0] - i[j-1][1] ==3:
                res.add(i[j][1]-i[j-1][0]+2)
            else:
                res.add(i[j][1]-i[j][0]+3)

    # print(d)
    return max(res)

for _ in range(readInt()):
    n = readInt()
    # a, b = intMap()
    arr = intList()
    
    print(f'Case #{_+1}: ',end='')
    print(solve(arr))
    # print('YES' if solve() else 'NO')