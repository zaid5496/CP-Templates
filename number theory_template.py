def compute_spf(n):        # O(nloglogn)
    spf = list(range(n + 1))  
    for i in range(2, int(n ** 0.5) + 1):
        if spf[i] == i:  # i is prime
            for j in range(i * i, n + 1, i):
                if spf[j] == j:
                    spf[j] = i
    return spf

def factorize(x, spf):    # O(logx)
    factors = {}
    while x != 1:
        p = spf[x]
        factors[p] = factors.get(p, 0) + 1
        x //= p
    return factors

def primefactors(n, spf):
    factors = []
    while n != 1:
        p = spf[n]
        factors.append(p)
        while n % p == 0:
            n //= p
    return factors

def generate(factors):            
    divisors = [1]
    for prime, exp in factors.items():
        current_divisors = []
        for d in divisors:
            for e in range(1, exp + 1):
                current_divisors.append(d * (prime ** e))
        divisors.extend(current_divisors)
    return sorted(divisors)

def get_divisors(x, spf):        # For numbers up to 10^6 the maximum number of divisors d(x) is 240
    factors = factorize(x, spf)
    return generate(factors)
