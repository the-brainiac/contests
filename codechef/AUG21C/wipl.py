# cook your dish here
# import sys
sys.setrecursionlimit(10**6)
def subset_sum(arr, value, n):
    if value == 0:
        return True
    if n <= 0:
        return False
        
    if (arr[n - 1] > value):
        key = (n-1, value)
        if key not in DP:
            DP[key] = subset_sum(arr, value, n-1)
        return DP[key]
        
    key = (n, value)
    
    if key not in DP:
        DP[key] = DP.get((n-1, value) , subset_sum(arr, value, n-1)) or DP.get((n-1, value-arr[n-1]) , subset_sum(arr, value-arr[n-1], n-1))
    
    return DP[key]

for _ in range(int(input())):
    n, k = map(int, input().split())
    boxes = sorted(list(map(int, input().split())), reverse=True)
    
    sh = 0
    min_boxes = 0
    for i in boxes:
        if sh >= 2*k:
            break
        
        sh += i
        min_boxes += 1
    
    possible = False
    DP = dict()
    while min_boxes <= n:
        for value in range(k, sh-k+1):
            possible = subset_sum(boxes, value, min_boxes)
            if possible:
                break
        if possible:
            break
        if min_boxes < n:
            sh += boxes[min_boxes]
        min_boxes += 1
        
    if possible:
        print(min_boxes)
    else:
        print(-1)