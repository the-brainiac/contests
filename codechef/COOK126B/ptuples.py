N = 10**6 +1
is_prime = [1]*N
is_prime[0] = 0
is_prime[1] = 0

def sieve():
    i = 2
    while i*i <= N:
        if is_prime[i] == 0:
            i += 1
            continue

        j = 2*i
        while j < N:
            is_prime[j] = 0
            # 
            j += i

        i += 1
sieve()

res = [0]*N
for i in range(5,N):
    res[i] = res[i-1]
    if is_prime[i] and is_prime[i-2]:
        res[i] += 1


for _ in range(int(input())):
    n = int(input())
    print(res[n])