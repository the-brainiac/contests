for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))
    d = dict()
    for i in range(n):
        d[arr[i]] = brr[i]
    arr.sort(key=lambda x:(d[x],-x))
    total = 0
    conv_pts = 0
    for i in arr:
        if total >= m:
            break
        total += i
        conv_pts += d[i]
    if total <m:
        print(-1)
    else:
        print(conv_pts)