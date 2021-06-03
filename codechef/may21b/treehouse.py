import math 
from collections import Counter, defaultdict
import sys, resource
resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10**6)
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


total_childs=[1]*(3*100001)

def dfs(graph,cur):
    
    for nbr in graph[cur]:
        
        dfs(graph,nbr)
        total_childs[cur]+=total_childs[nbr]
depth = Counter()
def dfs_depth(graph, cur):
    if len(graph[cur]) == 0:
        depth[cur] = 0
        return 0
    dpth = 0
    for data in graph[cur]:
        dpth = max(dpth, dfs_depth(graph, data))
    depth[cur] = dpth + 1
    return dpth + 1

width = Counter()
def dfs_width(graph, cur):
    if len(graph[cur]) == 0:
        width[cur] = 0
        return 0
    wdth = len(graph[cur])
    for data in graph[cur]:
        wdth = max(wdth, dfs_width(graph, data))
    width[cur] = wdth
    return wdth
    
leaves = Counter()
def dfs_leaves(graph, cur):
    if len(graph[cur]) == 0:
        leaves[cur] = 1
        return 1
    lvs = 0
    for data in graph[cur]:
        lvs += dfs_leaves(graph, data)
    leaves[cur] = lvs
    return lvs
    
keys = Counter()
def dfs_key(graph, cur):
    if len(graph[cur])==0:
        keys[cur] = 1
        return 1
    res = []
    for data in graph[cur]:
        res.append(dfs_key(graph, data))
    res.sort()
    kval = 1
    for i in range(len(res)):
        kval += (i+1)*res[i]
    keys[cur] = kval
    return kval 
    
def dfs2(graph, cur, parent):
    for data in graph[cur]:
        if data!=parent:
            dfs2(graph, data, cur)
    m = 1
    for data in sorted(graph[cur], key=lambda x: -sub_tree[x]):
        if data != parent:
            sub_tree[cur] += m * sub_tree[data]
            m += 1



for _ in range(readInt()):
    n, x = intMap()
    graph = defaultdict(list)

    for i in range(n-1):
        u, v = intMap()
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    # dfs_depth(graph, 0)
    # dfs_width(graph, 0)
    # dfs_leaves(graph, 0)
    # dfs_key(graph, 0)
    # print(width)
    # print(keys)
    # dfs(graph, 0)
    sub_tree = defaultdict(lambda:x)
    dfs2(graph, 0, -1)
    print(sub_tree[0]%mod)