import sys, math, heapq, bisect, random, secrets, copy, threading
from random import randint, getrandbits
from functools import cache, lru_cache
from collections import deque, Counter, defaultdict
from bisect import bisect_right, bisect_left
from types import GeneratorType
input = sys.stdin.readline
MOD = 998244353
SALT = random.getrandbits(32)
# sys.setrecursionlimit(1500)
inp = lambda: list(map(int, input().split()))
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
 
 
 
 
#-------------------------------------------------------------------------------------------------------------------# 
def divisors(x):
    front, rear = [], []
    for d1 in range(1, int(x**(0.5))+1): 
        if x%d1 == 0:
            d2 = x//d1
            front.append(d1)
            if d1 != d2:
                rear.append(d2)
                
    return front + rear[::-1]
    
    
    
    
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
