# 0-indexed
# used for idempodent operations such as min, max, GCD etc.

import math
class SparseTable:
    def __init__(self, arr):
        """
        Range Minimum Query (RMQ) with 0-based inclusive queries.
        Preprocessing: O(n log n)
        Query:        O(1)
        """
        self.n = len(arr)
        self.k = int(math.log2(self.n)) + 1              # max power
        self.st = [[0] * self.k for _ in range(self.n)]
        self.build(arr)

    def build(self, arr):                                # O(n logn)
        for i in range(self.n):
            self.st[i][0] = arr[i]
        for j in range(1, self.k):
            for i in range(self.n - (1 << j) + 1):
                self.st[i][j] = min(self.st[i][j-1], self.st[i + (1 << (j-1))][j-1])

    def query(self, l, r):                               # O(1)
        # Answer min from index l to r inclusive
        j = int(math.log2(r - l + 1))
        return min(self.st[l][j], self.st[r - (1 << j) + 1][j])

