from math import ceil
for _ in range(int(input())):
    n, k = map(int, input().split())
    if n%k == 0:
        print(1)
    else:
        v = (n+(k- n%k))
        print(ceil(v/n))