import math 
from collections import Counter, defaultdict
import sys, resource
resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10**6)


"""
# Template Designed By: Shivshanker Singh
# Note: If you find this template useful and want to use it then please don't just copy paste it 
		you can take ideas from this and make your own.
		because if you copy paste as it is then there are high chances that both of us will be plagiarized
		(because most of code will be same for small problems).
		So to avoid this please dont copy paste.
"""

mod       = 10**9 + 7
input     = sys.stdin.readline
readInt   = lambda : int(input().strip())
readfloat = lambda : float(input().strip())
readStr   = lambda : input().strip()
intList   = lambda : list(map(int, input().strip().split()))
intMap    = lambda : map(int, input().strip().split())
floatList = lambda : list(map(float, input().strip().split()))
floatMap  = lambda : map(float, input().strip().split())
strList   = lambda : list(input().strip().split())


def print(*args):
	for i in args:
		sys.stdout.write(str(i))
		sys.stdout.write(' ')
	sys.stdout.write('\n')

def simple_path_dfs(cur, parent):
    for child in graph[cur]:
        if child != parent:
            simple_path_dfs(child, cur)
            simple_path_count[cur] += 2*simple_path_count[child]

def remaining_path_dfs(cur, parent):
    global res
    total = (simple_path_count[cur]-1)//2
    for child in graph[cur]:
        if child != parent:
            remaining_path_dfs(child, cur)
            res += simple_path_count[child]*(total-simple_path_count[child])
    


for _ in range(readInt()):
    n = readInt()
    graph = defaultdict(list)

    for i in range(n-1):
        u, v = intMap()
        graph[u].append(v)
        graph[v].append(u)

    simple_path_count = defaultdict(lambda: 1)
    simple_path_dfs(1, 0)
    res = simple_path_count[1]
    remaining_path_dfs(1, 0)

    print(res%mod)