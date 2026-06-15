# https://codeforces.com/contest/1536/problem/D

from bisect import bisect_left as lower_bound
from bisect import bisect_right as upper_bound


class FenwickTree:
    def __init__(self, x):
        bit = self.bit = list(x)
        size = self.size = len(bit)
        for i in range(size):
            j = i | (i + 1)
            if j < size:
                bit[j] += bit[i]

    def update(self, idx, x):
        """updates bit[idx] += x"""
        while idx < self.size:
            self.bit[idx] += x
            idx |= idx + 1

    def __call__(self, end):
        """calc sum(bit[:end])"""
        x = 0
        while end:
            x += self.bit[end - 1]
            end &= end - 1
        return x

    def find_kth(self, k):
        """Find largest idx such that sum(bit[:idx]) <= k"""
        idx = -1
        for d in reversed(range(self.size.bit_length())):
            right_idx = idx + (1 << d)
            if right_idx < self.size and self.bit[right_idx] <= k:
                idx = right_idx
                k -= self.bit[idx]
        return idx + 1, k


class SortedList:
    block_size = 700

    def __init__(self, iterable=()):
        iterable = sorted(iterable)
        self.micros = [iterable[i:i + self.block_size - 1] for i in range(0, len(iterable), self.block_size - 1)] or [[]]
        self.macro = [i[0] for i in self.micros[1:]]
        self.micro_size = [len(i) for i in self.micros]
        self.fenwick = FenwickTree(self.micro_size)
        self.size = len(iterable)

    def insert(self, x):
        i = lower_bound(self.macro, x)
        j = upper_bound(self.micros[i], x)
        self.micros[i].insert(j, x)
        self.size += 1
        self.micro_size[i] += 1
        self.fenwick.update(i, 1)
        if len(self.micros[i]) >= self.block_size:
            self.micros[i:i + 1] = self.micros[i][:self.block_size >> 1], self.micros[i][self.block_size >> 1:]
            self.micro_size[i:i + 1] = self.block_size >> 1, self.block_size >> 1
            self.fenwick = FenwickTree(self.micro_size)
            self.macro.insert(i, self.micros[i + 1][0])

    def pop(self, k=-1):
        i, j = self._find_kth(k)
        self.size -= 1
        self.micro_size[i] -= 1
        self.fenwick.update(i, -1)
        return self.micros[i].pop(j)

    def __getitem__(self, k):
        i, j = self._find_kth(k)
        return self.micros[i][j]

    def count(self, x):
        return self.upper_bound(x) - self.lower_bound(x)

    def __contains__(self, x):
        return self.count(x) > 0

    def lower_bound(self, x):
        i = lower_bound(self.macro, x)
        return self.fenwick(i) + lower_bound(self.micros[i], x)

    def upper_bound(self, x):
        i = upper_bound(self.macro, x)
        return self.fenwick(i) + upper_bound(self.micros[i], x)

    def _find_kth(self, k):
        return self.fenwick.find_kth(k + self.size if k < 0 else k)

    def __len__(self):
        return self.size

    def __iter__(self):
        return (x for micro in self.micros for x in micro)

    def __repr__(self):
        return str(list(self))
        
        



sl = SortedList()                  # O(1)

# ---------------- Insert ----------------
sl.insert(30)                      # Amortized O(n^(1/3))
sl.insert(10)                      # Amortized O(n^(1/3))
sl.insert(20)                      # Amortized O(n^(1/3))
sl.insert(20)                      # Amortized O(n^(1/3))
sl.insert(40)                      # Amortized O(n^(1/3))

print(sl)                          # O(n)
# [10, 20, 20, 30, 40]

# ---------------- Lower Bound ----------------
print(sl.lower_bound(20))          # O(log(n/B) + log(B))
# 1

print(sl.lower_bound(25))          # O(log(n/B) + log(B))
# 3

# ---------------- Upper Bound ----------------
print(sl.upper_bound(20))          # O(log(n/B) + log(B))
# 3

print(sl.upper_bound(30))          # O(log(n/B) + log(B))
# 4

# ---------------- Count ----------------
print(sl.count(20))                # O(log(n/B) + log(B))
# 2

# ---------------- Contains ----------------
print(30 in sl)                    # O(log(n/B) + log(B))
# True

print(100 in sl)                   # O(log(n/B) + log(B))
# False

# ---------------- Indexing ----------------
print(sl[0])                       # O(log(n/B))
# 10

print(sl[3])                       # O(log(n/B))
# 30

print(sl[-1])                      # O(log(n/B))
# 40

# ---------------- Pop ----------------
print(sl.pop(2))                   # Amortized O(n^(1/3))
# 20

print(sl)                          # O(n)
# [10, 20, 30, 40]

# ---------------- Length ----------------
print(len(sl))                     # O(1)
# 4

# ---------------- Iteration ----------------
for x in sl:                       # O(n)
    print(x)





