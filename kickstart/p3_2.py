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
def get_max(brr):
    new_arr = []
    for i in range(1,n):
        new_arr.append(brr[i]-brr[i-1])
    if len(set(new_arr)) == 1 or len(set(new_arr))==2:
        return n
        
    res = 1
    temp = 1
    for i in range(1, len(new_arr)):
        if new_arr[i] == new_arr[i-1]:
            temp += 1
        else:
            res =  max(temp, res)
            temp = 1
    res =  max(temp, res)
    # print(new_arr, res)
    return res+1

def solve(arr):
    if n ==2:
        return 2
    res = set()
    for i in range(n-2):
        brr = arr.copy()
        brr[i] = arr[i+1] + arr[i+1] - arr[i+2]
        re = get_max(brr)
        if re == n:
            return re
        res.add(re)
    
    for i in range(n-1, 1, -1):
        brr = arr.copy()
        brr[i] = arr[i-1] - arr[i-2] + arr[i-1]
        re = get_max(brr)
        if re == n:
            return re
        res.add(re)
        
    return max(res)

for _ in range(readInt()):
    n = readInt()
    # a, b = intMap()
    arr = intList()
    
    print(f'Case #{_+1}: ',end='')
    print(solve(arr))
    # print('YES' if solve() else 'NO')