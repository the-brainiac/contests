for _ in range(int(input())):
    n = int(input())
    b = input().strip()
    res = ['1']
    for i in range(1,n):
        prev = res[-1]+b[i-1]
        if b[i] + '1' == prev or '1'+b[i] == prev:
            res.append('0')
        else:
            res.append('1')
    print(''.join(res))