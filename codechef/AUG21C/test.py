from itertools import chain, combinations

l = int(input())
li = list(map(int, input().split()))
s = int(input())

itr=chain.from_iterable(combinations(li, n) for n in range(len(li)+1))

result = [el for el in itr if sum(el)==s]

print(result)