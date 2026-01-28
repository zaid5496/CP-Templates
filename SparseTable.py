# 0-indexed
# used for idempodent operations such as min, max, GCD etc.

# https://codeforces.com/contest/1878/problem/E


class SparseTable: 
    def __init__(self, arr, func): 
        self.n = len(arr) 
        self.func = func 
        self.k = self.n.bit_length() 
        self.st = [[0] * self.n for _ in 
range(self.k)] 
        self.build(arr) 
 
    def build(self, arr):                             # O(N log N) 
        self.st[0] = arr[:] 
        for j in range(1, self.k): 
            step = 1 << j 
            half = step >> 1 
            for i in range(self.n - step + 1): 
                self.st[j][i] = self.func( 
                    self.st[j-1][i], 
                    self.st[j-1][i + half] 
                ) 
 
 
 
 
    def query(self, l, r):                            # O(1) 
        j = (r - l + 1).bit_length() - 1 
        return self.func( 
            self.st[j][l], 
            self.st[j][r - (1 << j) + 1] 
        )

# 0-indexed with [l, r] included
# used for idempodent operations such as 
# min, max, GCD, AND, OR etc. 
 
st = SparseTable(arr, min) 
ans = st.query(l, r)          # [l, r] included
st = SparseTable(arr, max) 
st = SparseTable(arr, math.gcd) 
st = SparseTable(arr, lambda a, b: a & b) 
st = SparseTable(arr, lambda a, b: a | b)




















# depricated :p
# import math
# class SparseTable:
#     def __init__(self, arr):
#         """
#         Range Minimum Query (RMQ) with 0-based inclusive queries.
#         Preprocessing: O(n log n)
#         Query:        O(1)
#         """
#         self.n = len(arr)
#         self.k = int(math.log2(self.n)) + 1              # max power
#         self.st = [[0] * self.k for _ in range(self.n)]
#         self.build(arr)

#     def build(self, arr):                                # O(n logn)
#         for i in range(self.n):
#             self.st[i][0] = arr[i]
#         for j in range(1, self.k):
#             for i in range(self.n - (1 << j) + 1):
#                 self.st[i][j] = min(self.st[i][j-1], self.st[i + (1 << (j-1))][j-1])

#     def query(self, l, r):                               # O(1)
#         # Answer min from index l to r inclusive
#         j = int(math.log2(r - l + 1))
#         return min(self.st[l][j], self.st[r - (1 << j) + 1][j])

