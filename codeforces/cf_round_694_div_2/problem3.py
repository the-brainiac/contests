for _ in range(int(input())):
    n, m = map(int, input().split())
    k = list(map(int, input().split()))
    prizes = list(map(int, input().split()))
    index_dict = dict()
    for i in range(m):
        index_dict[prizes[i]] = i
    c = prizes.copy()
    s = 0
    ma = max(prizes)
    for i in k:
        m = min(prizes[:i])
        if m < c[i-1]:
            s += m
            prizes[index_dict[m]] = ma
        else:
            s += c[i-1]
    print(s)