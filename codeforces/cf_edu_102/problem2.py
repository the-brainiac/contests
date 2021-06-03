from math import gcd
for _ in range(int(input())):
    s = input().strip()
    t = input().strip()
    n1 = len(s)
    n2 = len(t)
    lcm = (n1*n2)//gcd(n1, n2)
    flag = False
    for i in range(1, min(n1,n2)+1):
        res = s[:i]
        if len(s.replace(res, '')) == 0 and len(t.replace(res, '')) == 0:
            flag = True
            break
    if flag:
        print(res*(lcm//len(res)))
    else:
        print(-1)