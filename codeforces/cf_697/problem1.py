from math import log2
def solve(n):
    p = log2(n)
    if p!=int(p):
        return 'YES'
    return 'NO'

for _ in range(int(input())):
    n = int(input())
    print(solve(n))