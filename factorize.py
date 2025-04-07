def compute_spf(n):
    """
    Compute the SPF (smallest prime factor) for every number up to n.
    Returns a list spf where spf[i] is the smallest prime that divides i.
    """
    spf = list(range(n + 1))  # Initially, assume each number is its own SPF
    for i in range(2, int(n ** 0.5) + 1):
        if spf[i] == i:  # i is prime
            for j in range(i * i, n + 1, i):
                if spf[j] == j:
                    spf[j] = i
    return spf

def factorize(x, spf):
    """
    Factorize the number x using the SPF table.
    Returns a dictionary where keys are prime factors and values are their exponents.
    """
    factors = {}
    while x != 1:
        p = spf[x]
        factors[p] = factors.get(p, 0) + 1
        x //= p
    return factors

def primefactors(n, spf):
    """
    Returns a sorted list of distinct prime factors of n,
    using the precomputed SPF array and a while loop that divides out repeated factors.
    """
    factors = []
    while n != 1:
        p = spf[n]
        factors.append(p)
        # Divide out all factors of p:
        while n % p == 0:
            n //= p
    return factors

def generate_divisors_from_factors(factors):            
    """
    Generate all divisors from the prime factorization.
    'factors' is a dictionary with prime factors as keys and their exponents as values.
    """
    divisors = [1]
    for prime, exp in factors.items():
        current_divisors = []
        for d in divisors:
            for e in range(1, exp + 1):
                current_divisors.append(d * (prime ** e))
        divisors.extend(current_divisors)
    return sorted(divisors)

def get_divisors(x, spf):        #For numbers up to 10^6 the maximum number of divisors d(x) is 240
    """
    Get all divisors of x using the precomputed SPF table.
    """
    factors = factorize(x, spf)
    return generate_divisors_from_factors(factors)




limit = 10**6 + 1  
spf = compute_spf(limit)

x = 360  # Example number
divisors = get_divisors(x, spf)
print("Divisors of", x, "are:", divisors)
