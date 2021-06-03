f = open('input.txt', 'w')
res = map(str, range(2000))
f.write('100\n')
s = ' '.join(res)+'\n'
for i in range(100):
    f.write('2000\n')
    f.write(s)
f.close()