# 0-based indexed sparse table

# class SparseTable:
#     """
#     Range Minimum Query (RMQ) with 0-based inclusive queries.
#     Preprocessing: O(n log n)
#     Query:        O(1)
#     """
#     def __init__(self, arr):
#         self.n = len(arr)
#         # Precompute floor(log2) for lengths up to n
#         self.log = [0] * (self.n + 1)
#         for i in range(2, self.n + 1):
#             self.log[i] = self.log[i // 2] + 1

#         self.K = self.log[self.n] + 1
#         # st[k][i] = min over interval of length 2^k starting at i
#         self.st = [ [0] * self.n for _ in range(self.K) ]
#         self.st[0] = arr[:]  # level 0 is the original array

#         # Build higher levels
#         for k in range(1, self.K):
#             length = 1 << k
#             half   = length >> 1
#             for i in range(self.n - length + 1):
#                 self.st[k][i] = min(
#                     self.st[k-1][i],
#                     self.st[k-1][i + half]
#                 )

#     def query(self, l, r):
#         """
#         Returns min(arr[l..r]), where 0 <= l <= r < n.
#         """
#         if l < 0 or r >= self.n or l > r:
#             raise IndexError(f"Invalid RMQ query range [{l}, {r}]")
#         length = r - l + 1
#         k = self.log[length]
#         half = 1 << k
#         return min(
#             self.st[k][l],
#             self.st[k][r - half + 1]
#         )


# 0-indexed
# used for idempodent operations such as min, max, GCD etc.

import math
class SparseTable:
    def __init__(self, arr):
        self.n = len(arr)
        self.k = int(math.log2(self.n)) + 1  # max power
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

