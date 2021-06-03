from math import ceil

for _ in range(int(input())):
    n, k = map(int, input().split())
    prr = list(map(int, input().split()))
    res = 0
    s = prr[0]
    for i in range(1, n):
        if prr[i]/s > k/100:
            val = ceil(((100*prr[i])/k) - s)
            res += val
            s += val
        s += prr[i]
    print(res)