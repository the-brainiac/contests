# cook your dish here
for i in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    res1 = 0
    res2 = 0
    for i in arr:
        if i%2:
            res1 += 1
        else:
            res2 += 1
    
    print(min(res1, res2))