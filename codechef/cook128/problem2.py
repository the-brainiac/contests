import math 
from collections import Counter, defaultdict
import sys
sys.setrecursionlimit(10**6)

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

def findAndSum(arr, n):
	Sum = 0
	mul = 1

	for i in range(30):
		count_on = 0
		l = 0
		for j in range(n):

			if ((arr[j] & (1 << i)) > 0):
				if (count_on):
					l += 1
				else:
					count_on = 1
					l += 1

			elif (count_on):
				Sum |= ((mul * l * (l + 1)) // 2)
				count_on = 0
				l = 0
			
		if (count_on):
			Sum |= ((mul * l * (l + 1)) // 2)
			count_on = 0
			l = 0
		
		mul *= 2
	
	return Sum



for _ in range(readInt()):
    n = readInt()
    a, b = intMap()
    arr = intList()
    
    print('YES' if solve() else 'NO')