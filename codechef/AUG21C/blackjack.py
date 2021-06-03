
def get_subsets_rec(arr, n, v, sum): 
	if n == 0 and sum != 0 and dp[0][sum]: 
		v.add(arr[n])
		res.append(v) 
		return

	if n == 0 and sum==0:
	    res.append(v)
	    return

	if dp[n-1][sum]:
	    b = v.copy()
	    get_subsets_rec(arr, n-1, b, sum) 
	
	if sum >= arr[n] and dp[n-1][sum-arr[n]]:
	    v.add(arr[n]) 
	    get_subsets_rec(arr, n - 1, v , sum - arr[n])


def make_dp(arr, n, value):
    dp = [[False for i in range(value+1)] for j in range(n+1)]
    for i in range(n+1):
        dp[i][0] = True
    
    if arr[0] <= value:
        dp[0][arr[0]] = True
    
    for i in range(1, n):
        for j in range(1, value+1):
            if arr[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i]]
    return dp

def get_subsets(arr, n, value):
    if dp[n-1][value] == False:
        return
    get_subsets_rec(arr, n-1, set(), value)


for _ in range(int(input())):
    n, x, y = map(int, input().split())
    arr = list(map(int, input().split()))
    dp = make_dp(arr, n, y)
    min_swaps = n+1
    for value in range(x, y+1):
        res = []
        get_subsets(arr, n, value)
        if len(res) == 0:
            continue
        swaps = 0
        s = res[0]
        for i in range(len(s)):
            if arr[i] not in s:
                swaps += 1
        min_swaps = min(min_swaps, swaps)
        break
    if min_swaps < n+1:
        print(min_swaps)
    else:
        print(-1)