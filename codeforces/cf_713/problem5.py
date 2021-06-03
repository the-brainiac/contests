import math 
from collections import Counter, defaultdict, deque
import gc

readInt   = lambda : int(input().strip())
readfloat = lambda : float(input().strip())
intList   = lambda : list(map(int, input().strip().split()))
intMap    = lambda : map(int, input().strip().split())
floatList = lambda : list(map(float, input().strip().split()))
floatMap  = lambda : map(float, input().strip().split())


# N = 10**5
# is_prime = [1]*N
# is_prime[0] = 0
# is_prime[1] = 0

def sieve():
    i = 2
    while i*i <= N:
        if is_prime[i] == 0:
            i += 1
            continue

        j = 2*i
        while j < N:
            is_prime[j] = 0
            j += i

        i += 1
# sieve()

class Pair:
    psf = set()
    def __init__(self, i, j, psf):
        self.i = i
        self.j = j
        self.psf = psf

def get_subsets_rec(arr, n, value): 
    queue = deque()
    queue.append(Pair(n, value, set()))

    while len(queue) > 0:
        rem = queue.popleft()
        if rem.i == 0 or rem.j == 0:
            res.append(rem.psf)
        else:
            exc = dp[rem.i - 1][rem.j]
            if exc:
                queue.append(Pair(rem.i-1, rem.j, rem.psf))

            if rem.j >= arr[rem.i-1]:
                inc = dp[rem.i - 1][rem.j - arr[rem.i -1]]
                if inc:
                    b = rem.psf.copy()
                    b.add(rem.i - 1)
                    queue.append(Pair(rem.i - 1, rem.j-arr[rem.i-1], b))
            
def make_dp(arr, n, value):
    dp = [[False for i in range(value+1)] for j in range(n+1)]
    
    for i in range(n+1):
        for j in range(value+1):
            if j ==0:
                dp[i][j] = True
            elif i == 0:
                dp[i][j] = False
            else:
                if dp[i-1][j]:
                    dp[i][j] = True
                elif j >=arr[i-1]:
                    if dp[i-1][j-arr[i-1]]:
                        dp[i][j] = True
    return dp

def get_subsets(arr, n, value):
    if dp[n][value] == False:
        return []
    global res
    res = []
    get_subsets_rec(arr, n, value)
    return res

def solve(l, r, s):
    arr = range(1, n+1)
    global dp
    dp = make_dp(arr, n, s)
    res = get_subsets(arr, n, s)
    d = defaultdict(list)
    for subset in res:
        d[len(subset)].append(subset)

    if r-l+1 not in d:
        return -1

    final_arr = [] 
    interval = d[r-l+1][0]
    s_interval = set(interval)
    ls = []
    del dp
    del res
    del d
    gc.collect()
    
    for i in arr:
        if i-1 not in s_interval:
            ls.append(i)
    i = 0
    idx = 0
    while i < n:
        if i >= l-1 and i <r:
            for j in interval:
                final_arr.append(j+1)
                i += 1
        else:
            final_arr.append(ls[idx])
            idx += 1
            i += 1
    return final_arr

for _ in range(readInt()):
    # n = readInt()
    n, l, r, s = intMap()
    res = solve(l, r, s)
    if res == -1:
        print(res)
    else:
        print(*res)