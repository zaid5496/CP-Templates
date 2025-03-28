MOD = 10**9 + 7
MAX = 10**6  # adjust this according to the constraints of the problem..!!
def precompute_factorials(MAX, MOD):
    """ Precomputes factorials and inverse factorials up to n """
    fact = [1]*(MAX + 1)
    for i in range(2, MAX + 1):
        fact[i] = (fact[i - 1] * i) % MOD
    
    inv = [1]*(MAX + 1)
    inv[MAX] = pow(fact[MAX], MOD - 2, MOD)
    for i in range(MAX - 1, 0, -1):
        inv[i] = (inv[i + 1] * (i + 1)) % MOD

    return fact, inv

def C(n, r):
    """ Computes binomial coefficient C(n, r) = nCr % MOD """
    if r > n or r < 0:
        return 0
    return (fact[n] * inv[r] % MOD) * inv[n - r] % MOD

def P(n, r):
    """Computes the permutation count P(n, r) = nPr modulo MOD."""
    if r > n or r < 0:
        return 0
    return (fact[n] * inv[n - r]) % MOD

fact, inv = precompute_factorials(MAX, MOD)


print(C(10, 3))  # Output: 120
print(C(5, 2))   # Output: 10
print(P(5, 2))   # Output: 20
    
# when we take modulo by a MOD the remainder is the answer eg (a%MOD),
# but when the items are in denomenator as well it is not possible so we invert them,
# for eg: nCr%MOD = (n!)*((n-r)!)^(-1)*(r!)^(-1), we calculate r^(-1) using the modular inverse property of fermat's little theorem
# fermat's little theorem states that for any integer a and a prime p, 
# a^p = a(modp)
# a^(p-1) = 1(modp)
# multiplying a^(-1) on both the sides, we get:
# a^(-1)(modp) = a^(p-2)
