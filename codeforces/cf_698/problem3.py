def check(d,n):
    
for _ in range(int(input())):
    n = input()
    d = list(map(int, input().split()))
    if check(d,n):
        print('YES')
    else:
        print('NO')