class MergeSortTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.arr = arr
        self.seg = [[] for _ in range(4 * self.n)]  # Each node will hold a sorted list

    def build_tree(self, i=0, low=0, high=None):
        if high is None:
            high = self.n - 1

        if low == high:
            self.seg[i] = [self.arr[low]]
            return self.seg[i]

        mid = (low + high) // 2
        left = self.build_tree(2 * i + 1, low, mid)
        right = self.build_tree(2 * i + 2, mid + 1, high)
        self.seg[i] = sorted(left + right)

        return self.seg[i]

    # Count of elements ≤ x in range [l, r]
    def query(self, l, r, x, i=0, low=0, high=None):
        if high is None:
            high = self.n - 1

        if r < low or high < l:
            return 0  # No overlap

        if l <= low and high <= r:
            # Fully within query range
            return bisect.bisect_right(self.seg[i], x)

        mid = (low + high) // 2
        left = self.query(l, r, x, 2 * i + 1, low, mid)
        right = self.query(l, r, x, 2 * i + 2, mid + 1, high)
        return left + right
