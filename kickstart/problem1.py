for t in range(int(input())):
    n = int(input())
    s = input().strip()
    res = [1]
    temp = 1
    for i in range(1, n):
        if s[i] > s[i-1]:
            temp += 1
        else:
            temp = 1
        res.append(temp)
    print(f'Case #{t+1}: ',end='')
    print(*res)