for _ in range(int(input())):
    n, d = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    if max(a) <= d or a[0] + a[1] <= d:
        print('yes')
    else:
        print('no')