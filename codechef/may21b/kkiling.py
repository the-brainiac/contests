import math 
from collections import Counter, defaultdict
import sys, resource
resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10**6)

"""
# Template Designed By: the_brainiac (Shivshanker Singh)
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


def solve():
    pass

def dfs(cur, parent):
    if len(graph[cur]) == 1 and graph[cur][0]==parent:
        res[cur]['days'] = 0
        res[cur]['path'].append(cur)
        return

    res[cur]['days'] = 10**6
    days = []
    for node in graph[cur]:
        if node!=parent:
            dfs(node, cur)
            res[cur]['days'] = min(res[node]['days']+1, res[cur]['days'])
            days.append(res[node]['days'])
    
    c = Counter(days)
    l = len(c)
    minc = min(c)
    min_day = res[cur]['days']
    for node in graph[cur]:
        if node != parent:
            if c[minc]>1 or cur==1:
                if res[node]['days'] == minc:
                    for path in res[node]['path']:
                        res[cur]['path'].append(path)
            else:
                if res[node]['days'] > min(c) or l ==1:
                    for path in res[node]['path']:
                        res[cur]['path'].append(path)
                    if l > 1: 
                        res[cur]['days'] = min_day +1


    

def func():
    return {'days':1, 'path':[]}

# if __name__ == '__main__':
for _ in range(readInt()):
    n = readInt()
    graph = defaultdict(list)

    for i in range(n-1):
        u, v = intMap()
        graph[u].append(v)
        graph[v].append(u)

    res = defaultdict(func)
    dfs(1,0)
    # print(res)
    print(len(res[1]['path']), res[1]['days'])
    print(*sorted(res[1]['path']))