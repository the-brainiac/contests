from collections import deque

class Pair:
    def __init__(self, i, j, path_set):
        self.i = i
        self.j = j
        self.path_set = path_set

def get_subsets(arr, n, value): 
    """
    This function appends all the possible paths in result list for the given target sum
    Arguments:
        arr = A list of numbers
        n = number of elements in that list arr
        value = Target sum for which we want to generate table
    """
    # return immediately if there is no possible subset in arr whose sum is equal to value
    if dp[n][value] == False:
        return
        
    queue = deque()
    queue.append(Pair(n, value, set()))

    while len(queue) > 0:
        pair = queue.popleft()
        if pair.i == 0 or pair.j == 0:
            result.append(pair.path_set)
        else:
            exclude = dp[pair.i - 1][pair.j]
            if exclude:
                queue.append(Pair(pair.i-1, pair.j, pair.path_set))

            if pair.j >= arr[pair.i-1]:
                include = dp[pair.i - 1][pair.j - arr[pair.i -1]]
                if include:
                    b = pair.path_set.copy()
                    b.add(pair.i - 1)
                    queue.append(Pair(pair.i - 1, pair.j-arr[pair.i-1], b))
            

def make_dp(arr, n, value):
    """
    This function makes a table of target sum equal to the value
    Arguments:
        arr = A list of numbers
        n = number of elements in that list arr
        value = Target sum for which we want to generate table
    Returns:
        dp = A 2D boolean table
    """
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

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    value = int(input())
    dp = make_dp(arr, n, value)
    result = []
    get_subsets(arr, n, value)
    print(result)

# for _ in range(int(input())):
#     n, x, y = map(int, input().split())
#     arr = list(map(int, input().split()))
#     dp = make_dp(arr, n, y)
#     min_swaps = n+1
#     for value in range(x, y+1):
#         result = []
#         get_subsets(arr, n, value)
#         for s in result:
#             swaps = 0
#             for i in range(len(s)):
#                 if i not in s:
#                     swaps += 1
#             min_swaps = min(min_swaps, swaps)
#     if min_swaps < n+1:
#         print(min_swaps)
#     else:
#         print(-1)