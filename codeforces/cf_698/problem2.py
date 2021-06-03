def check(n, d):
    
    ds = str(d)
    while n > 0:
        s = set(str(n))
        if ds in s:
            return True
        n -= d
    return False


for _ in range(int(input())):
    n, d = map(int,input().split())
    arr = list(map(int,input().split()))
    for i in arr:
        if check(i,d):
            print('YES')
        else:
            print('NO')