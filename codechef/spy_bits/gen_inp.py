import random

f = open('input.txt', 'w')
n = random.randint(1,10**5)
res = [str(random.randint(1,10**9)) for i in range(n)]
f.write(str(n)+'\n')
f.write(' '.join(res)+'\n')
q = random.randint(1,10**5)
f.write(str(q)+'\n')
for i in range(q):
    x = random.randint(1,n)
    k = random.randint(1,10**9)
    f.write(str(x)+' '+str(k)+'\n')
f.close()