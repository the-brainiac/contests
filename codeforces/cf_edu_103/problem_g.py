n, m = map(int, input().split())
arr = list(map(int, input().split()))
for q in range(m):
    query = list(map(int, input().split()))
    if q[0] == 1:
        l, r, k = query[1], query[2], query[3]
    else:
        p, x = query[1], query[2]
        arr[p-1] = x