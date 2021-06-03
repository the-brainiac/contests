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
class Graph: 
 
    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]
         
    def addEdge(self, src, des):
  
        self.adj[src].append(des)
        self.adj[des].append(src)
  
    def minEdgeDFs(self, visited, src, des, min_edges, edge_count):
        visited[src] = True
        if src == des:
            if min_edges > edge_count:
                min_edges = edge_count
          
        else: 
            for v in self.adj[src]: 
                 
                if not visited[v]: 
                    edge_count += 1
     
                    min_edges, edge_count = self.minEdgeDFs(visited, v, des, min_edges, edge_count)
                  
        visited[src] = False
        edge_count -= 1
        return min_edges, edge_count
      
    def minEdge(self, u, v):
        visited = [False] * self.V
        min_edges = float('inf')
        edge_count = 0
     
        min_edges, edge_count = self.minEdgeDFs(visited, u, v, min_edges, edge_count)
     
        return min_edges
  

for _ in range(readInt()):
    # n = readInt()
    n, k, a = intMap()
    krr = intList()
    krr.sort()
    res1 = []
    res2 = []
    g = Graph(n)
    for i in range(n-1):
        u, v = intMap()
        g.addEdge(u-1,v-1)
    d = dict()
    for u in krr:
        d[u] = g.minEdge(a-1, u-1)
    for i in range(n):    
        temp = -10**9
        tu = 0
        for u in krr:
            dist = d[u] - g.minEdge(i,u-1)
            if dist > temp:
                temp = dist
                tu = u
        res1.append(temp)
        res2.append(tu)

    print(*res1)
    print(*res2)