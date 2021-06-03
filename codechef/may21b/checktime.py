l = [0]
i = 0
while len(l) > 0:
    if i == 45*10**5:
        break
    i += 1
    l.append(i)
    l.pop(0)