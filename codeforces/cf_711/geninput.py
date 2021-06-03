f = open('input.txt', 'w')
f.write('100000 1000000000\n')
n = 2**18
for i in range(10**5):
    f.write(str(n)+' ')
f.close()