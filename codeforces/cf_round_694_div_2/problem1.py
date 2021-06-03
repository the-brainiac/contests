from math import ceil
for _ in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    max_val = 0
    for i in a:
        max_val += ceil(i/x)
    min_val = ceil(sum(a)/x)
    print(min_val, max_val)