from collections import Counter
def solve(arr, n):
    # res = 1
    # for i in range(1,n):
    #     if arr[i] == arr[i-1]:
    #         res += 1
    # return res
    return max(Counter(arr).values())

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    print(solve(arr, n))