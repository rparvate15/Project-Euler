
def sumPrimes(n):
    sum, primes = 0, [True] * n
    for p in range(2, n):
        if primes[p]:
            sum += p
            for i in range(p*p, n, p):
                primes[i] = False
    return sum

print(sumPrimes(2000000))