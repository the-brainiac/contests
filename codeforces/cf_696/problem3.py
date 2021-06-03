for _ in range(int(input())):
    n, m = map(int, input().split())
    s = input().strip()
    for q in range(m):
        x = 0
        res = set()
        res.add(x)
        l, r = map(int, input().split())
        # print(s[:l-1]+s[r:])
        for i in s[:l-1]+s[r:]:
            if i =='+':
                x += 1
            if i == '-':
                x -= 1
            res.add(x)
        print(len(res))