for _ in range(int(input())):
    n = int(input())
    s = input()
    opr = ''
    for i in s:
        if i== 'R':
            opr += 'L'
        else:
            opr += 'R'
    