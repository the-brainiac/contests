for _ in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    i = 0
    while i < len(a):
        if a[i] % x:
            break
        a += [a[i]//x]*x
        i += 1
    print(sum(a))