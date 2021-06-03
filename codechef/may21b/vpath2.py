from collections import defaultdict
import sys, resource
resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10**6)

mod = 10**9 + 7

def dfs(cur, prev):
    dp[cur] = 1
    total[cur] = 1
    s = 0
    for data in graph[cur]:
        if data!= prev:
            dfs(data, cur)
            dp[cur] += 2*dp[data]
            total[cur] += total[data] + dp[data]
            s += dp[data]
    for data in graph[cur]:
        if data!= prev:
            total[cur] += dp[data]*(s-dp[data])

for _ in range(int(input())):
    n = int(input())
    graph = defaultdict(list)

    for i in range(n-1):
        u, v = map(int, input().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    dp = [0]*(n+5)
    total = [0]*(n+5)
    dfs(0, -1)
    # print(dp)
    # print(total)
    print(total[0]%mod)
    # print(len(final_set)%mod)