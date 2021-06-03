# cook your dish here
for i in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    if sum(arr)%2:
        print(2)
    else:
        print(1)