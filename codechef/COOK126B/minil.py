for _ in range(int(input())):
    n, m = map(int, input().split())
    min1 = 0
    star1 = 0
    star2 = 0
    min2 = 0
    for i in range(n):
        s = input().strip()
        if i%2:
            for j in range(m):
                if j%2:
                    if s[j] == '*':
                        min1 += 1
                    else:
                        star2+=1
                        min2 += 1
                else:
                    if s[j] == '.':
                        star1+=1
                        min1 += 1
                    else:
                        min2 += 1
        else:
            for j in range(m):
                if j%2:
                    if s[j] == '*':
                        min2 += 1
                    else:
                        min1 += 1
                else:
                    if s[j] == '.':
                        min2 += 1
                    else:
                        min1 += 1
    if m%2==0:
        print(min(min1, min2))
    else:
        print(min2)