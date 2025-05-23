# 0-based indexed sparse table

class SparseTable:
    """
    Range Minimum Query (RMQ) with 0-based inclusive queries.
    Preprocessing: O(n log n)
    Query:        O(1)
    """
    def __init__(self, arr):
        self.n = len(arr)
        # Precompute floor(log2) for lengths up to n
        self.log = [0] * (self.n + 1)
        for i in range(2, self.n + 1):
            self.log[i] = self.log[i // 2] + 1

        self.K = self.log[self.n] + 1
        # st[k][i] = min over interval of length 2^k starting at i
        self.st = [ [0] * self.n for _ in range(self.K) ]
        self.st[0] = arr[:]  # level 0 is the original array

        # Build higher levels
        for k in range(1, self.K):
            length = 1 << k
            half   = length >> 1
            for i in range(self.n - length + 1):
                self.st[k][i] = min(
                    self.st[k-1][i],
                    self.st[k-1][i + half]
                )

    def query(self, l, r):
        """
        Returns min(arr[l..r]), where 0 <= l <= r < n.
        """
        if l < 0 or r >= self.n or l > r:
            raise IndexError(f"Invalid RMQ query range [{l}, {r}]")
        length = r - l + 1
        k = self.log[length]
        half = 1 << k
        return min(
            self.st[k][l],
            self.st[k][r - half + 1]
        )
