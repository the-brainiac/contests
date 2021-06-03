N = 10**5
is_prime = [1]*N
# We know 0 and 1 are composites
is_prime[0] = 0
is_prime[1] = 0

def sieve():
    """
    We cross out all composites from 2 to sqrt(N)
    """
    i = 2
    # This will loop from 2 to int(sqrt(x))
    while i*i <= N:
        # If we already crossed out this number, then continue
        if is_prime[i] == 0:
            i += 1
            continue

        j = 2*i
        while j < N:
            # Cross out this as it is composite
            is_prime[j] = 0
            # j is incremented by i, because we want to cover all multiples of i
            j += i

        i += 1
sieve()

def nextPrime(n):
    i = n
    while True:
        if is_prime[i]:
            return i
        i += 1

for _ in range(int(input())):
    d = int(input())
    k1 = nextPrime(d+1)
    k2 = nextPrime(d+k1)
    print(k1*k2)