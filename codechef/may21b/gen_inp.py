import random
def write(*args):
    for i in args:
        f.write(str(i)+' ')
    f.write('\n')
f = open('input.txt', 'w')
t = random.randint(1,3)
write(t)
for i in range(t):
    # n = random.randint(200000,300000)
    n = 100000
    write(n)
    for u in range(1, n):
        write(u,u+1)
f.close()