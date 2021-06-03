from collections import Counter
from math import factorial as fact

def nCr(n, r):
    if r>n:
        return 0
    return fact(n) // ( fact(r) * fact(n - r))

for _ in range(int(input())):
    a,b,k = map(int, input().split())
    arr = Counter(map(int, input().split()))
    brr = Counter(map(int, input().split()))
    arr_counter = Counter(arr)
    brr_counter = Counter(brr)
    print(arr_counter, brr_counter)
    same = 0
    for i in arr_counter:
        same += arr_counter[i] - 1
    for i in brr_counter:
        same += brr_counter[i] - 1
    print(nCr(k,2)- nCr(same, 2))