# cook your dish here
for _ in range(int(input())):
    n = int(input())
    s = [1 if i=='+' else -1 for i in input()]
    la=[0]*n
    lb=[0]*n
    lc=[0]*n
    a=b=c=0
    for i in range(1, n):
        c += s[i-1]
        a = min(a, c)
        b = max(b, c)
        la[i], lb[i], lc[i] = a, b, c
 
    a=b=c=0
    ra=[0]*n
    rb=[0]*n
 
    for i in range(n-2, -1, -1):
        a , b = min (0, a + s[i+1]) , max(0, b + s[i+1])
        ra[i], rb[i] = a, b
 
    print(max(lb[0],rb[n]+lc[0]))