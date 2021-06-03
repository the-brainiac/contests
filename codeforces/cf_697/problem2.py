def solve(n):
    a = n//2020
    for x in range(a+1):
        y = a-x
        if (2020*(x+y)) +y == n:
            return 'YES'
    return 'NO'
for _ in range(int(input())):
    n = int(input())
    print(solve(n))