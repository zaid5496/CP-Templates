import sys, math, heapq, bisect, random, secrets, copy, threading, itertools
from random import randint, getrandbits
from functools import cache, lru_cache        # comment out for cses
from collections import deque, Counter, defaultdict
from bisect import bisect_right, bisect_left
from types import GeneratorType



'''
--- FILE I/O SWITCH: if filenames passed, use them ---
Usage:
  python solution.py                # read from stdin, write to stdout
  python solution.py input.txt      # read from input.txt, write to stdout
  python solution.py input.txt out.txt  # read input.txt, write to out.txt
'''
if len(sys.argv) >= 2:
    sys.stdin = open(sys.argv[1], 'r')
if len(sys.argv) >= 3:
    sys.stdout = open(sys.argv[2], 'w')



input = sys.stdin.readline
MOD = 998244353
SALT = random.getrandbits(32)
# sys.setrecursionlimit(1500)    
    
ii = lambda: int(input())
inp = lambda: list(map(int, input().split()))
inp1 = lambda: list(map(lambda x:int(x)-1, input().split()))
# INF = float('inf')
INF = 1<<60
# SALT = 0
 

 
 
# -------------------------------------------------------------------------------------------------------------------#
from types import GeneratorType
 
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:           
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc
 
 
def divisors(x):
    front, rear = [], []
    for d1 in range(1, int(x**(0.5))+1): 
        if x%d1 == 0:
            d2 = x//d1
            front.append(d1)
            if d1 != d2:
                rear.append(d2)
                
    return front + rear[::-1]
 
def myhash(a, b):
    return ((a+b)*(a+b+1))//2 + b    
 
def sieve(n):
    prime = [True]*(n+1)
    prime[0:2] = [False, False]
    
    for i in range(2, int(n**0.5) + 1):
        if prime[i] == False:
            continue
        for j in range(i*i, n+1, i):
            prime[j] = False
            
    return [i for i, x in enumerate(prime) if x]
    
 
def compute_spf(n):
    spf = list(range(n+1))
    
    for i in range(2, int(n**0.5) + 1):
        if spf[i] != i: 
            continue
        for j in range(i*i, n+1, i):
            spf[j] = i
            
            
    return spf
    
 
 
def factorize(x):
    factors = {}
    
    while x != 1:
        p = spf[x]
        factors[p] = factors.get(p, 0) + 1
        x//= p
            
    return factors
    
 
def lcm(a, b):
    return (a*b)//math.gcd(a,b)
    
 
MOD = 10**9 + 7
MAX = 10**6 + 50  # adjust this according to the constraints of the problem..!!
def precompute_factorials(MAX, MOD):
    fact = [1]*(MAX+1)
    for i in range(2, MAX+1):
        fact[i] = (fact[i-1]*i) % MOD
    
    inv = [1]*(MAX+1)
    inv[MAX] = pow(fact[MAX], MOD-2, MOD)
    for i in range(MAX-1, 0, -1):
        inv[i] = (inv[i+1]*(i+1)) % MOD
 
    return fact, inv
 

def C(n, r):
    if r > n or r < 0:
        return 0
    return (fact[n] * inv[r] % MOD) * inv[n-r] % MOD
 
 
 
def P(n, r):
    if r > n or r < 0:
        return 0
    return (fact[n] * inv[n-r]) % MOD
        
    
# fact, inv = precompute_factorials(MAX, MOD)
# spf = compute_spf(10**6+1) 
# primes = sieve(10**6 + 1)
# -------------------------------------------------------------------------------------------------------------------#
 
'''
idea : 
       
       
'''
# -------------------------------------------------------------------------------------------------------------------#        
        
        
# T = 1
T = int(input())
for tc in range(1, T+1):
    print('Master : smz.26')
        










    
    
    
    
# wrapper for XORing in set and dictionary :O
#-------------------------------------------------------------------------------------------------------------------#
class MyDict:
    def __init__(self, func=lambda: 0):
        self.random = getrandbits(64)
        self.default = func
        self.dict = {}
    def __getitem__(self, key):
        my_key = self.random ^ key
        if my_key not in self.dict:
            self.dict[my_key] = self.default()
        return self.dict[my_key]
    def __setitem__(self, key, value):
        my_key = self.random ^ key
        self.dict[my_key] = value
    def __delitem__(self, key):
        my_key = self.random ^ key
        del self.dict[my_key]
    def __contains__(self, key):
        return (self.random ^ key) in self.dict
    def __len__(self):
        return len(self.dict)
    def __iter__(self):
        # Iterate over original keys
        for k in self.dict:
            yield self.random ^ k
    def get(self, key, default=None):
        my_key = self.random ^ key
        return self.dict.get(my_key, default)
    def pop(self, key, default=None):
        my_key = self.random ^ key
        return self.dict.pop(my_key, default)
    def keys(self):
        return [self.random ^ k for k in self.dict.keys()]
    def values(self):
        return list(self.dict.values())
    def items(self):
        return [(self.random ^ k, v) for k, v in self.dict.items()]
    def clear(self):
        self.dict.clear()
    def __str__(self):
        return str(self.items())
    def __repr__(self):
        return f"MyDict({self.items()})"
        
        
        
        
#-------------------------------------------------------------------------------------------------------------------#        
class MySet:
    def __init__(self, iterable=None):
        self.random = getrandbits(64)
        self.set = set()
        if iterable is not None:
            for key in iterable:
                self.add(key)
    def add(self, key):
        self.set.add(self.random ^ key)
    def discard(self, key):
        self.set.discard(self.random ^ key)
    def remove(self, key):
        self.set.remove(self.random ^ key)
    def __contains__(self, key):
        return (self.random ^ key) in self.set
    def __len__(self):
        return len(self.set)
    def __iter__(self):
        for k in self.set:
            yield self.random ^ k
    def __str__(self):
        return str([self.random ^ k for k in self.set])
    def __repr__(self):
        return f"MySet({list(self)})"
