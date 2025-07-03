# n=100
# prime=[True for i in range(n+1)]
# p=2
# while p*p<=n:
#     if prime[p]==True:
#         for i in range(p*p,n+1,p):
#             prime[i]=False
#     p+=1
# isPrime=[]
# for i in range(2,len(prime)):
#     if prime[i]==True:
#         isPrime.append(i)
# print(isPrime)

def sieve(n):
    """
    Return a list of all primes <= n using the Sieve of Eratosthenes.
    """
    is_prime = [True] * (n+1)
    is_prime[0:2] = [False, False]  # 0 and 1 are not prime
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    return [i for i, prime in enumerate(is_prime) if prime]

# Example usage:
# primes_up_to_100 = sieve(100)
