def subset_sum(arr, sum, n):
    if sum == 0:
        return True
    if n <= 0:
        return False
        
    if (arr[n - 1] > sum):
        return False
        
    key = (n, sum)
    if key not in DP:
        DP[key] = DP.get((n-1, sum) , subset_sum(arr, sum, n-1)) or DP.get((n-1, sum-arr[n-1]) , subset_sum(arr, sum-arr[n-1], n-1))
    
    return DP[key]

def table_subset_sum(arr, sum , n):
    for i in range(n+1):
        DP[(i, 0)] = True
    
    for i in range(sum+1):
        DP[(0, i)] = False
    
    for i in range(1, n+1):
        for j in range(1, sum+1):
            if arr[i-1] > j:
                DP[(i, j)] = DP[(i-1, j)]
            else:
                DP[(i, j)] = DP[(i-1, j)] or DP[(i-1, j-arr[i-1])]
    return DP[(n, sum)]

def foo(arr , s) : 
    ll = [0]
    for i in arr : 
        for j in range(len(ll)) : 
            if(ll[j] + i <= s) : 
                ll.append(ll[j] + i)
                if(ll[j] + i == s) : 
                    print(1)
                    return True
    return False

def Solve(arr, value, n):
    dp = [False] * (value + 1)
    dp[0] = True
    for i in range(n):
        for j in range(value - arr[i], -1, -1):
            if dp[j]:
                dp[j + arr[i]] = True
            # if dp[value]:
                # return True
    # return False
    return dp[value]

DP = dict()
n, sum = map(int, input().split())
arr = list(map(int, input().split()))
# print(subset_sum(arr, sum, n))
print(table_subset_sum(arr, sum, n))
# print(Solve(arr, sum, n))
# print(DP[(10,5)])