# 0-based indexing wala code he apna
# apne segtree me [l, r] dono included rehte he

class segtree:
    def __init__(self, n):
        self.seg = [0]*(4*n)
        self.n = n
        
    def build_tree(self, arr, i=0, low=0, high=None):    # low and high are the segments of the segtree
                                                         # desi bhasha me bole to upper bound aur lower bound
        if high is None:
            high = self.n - 1
            
        if low == high:                                  # ye condition hit hui mtlb ke root node(i - i wala) aa gya
            self.seg[i] = arr[low]
            return self.seg[i]                           # pachi ye value(i-i node ki value arr ka single element) ko return kar dia for further segment sum
        
        mid = (low + high)//2                            # nai to mid nikala left aur right subtree me dhundha
        left = self.build_tree(arr, 2*i + 1, low, mid)
        right = self.build_tree(arr, 2*i + 2, mid + 1, high)
        
        self.seg[i] =  left + right                      # segment sum
        
        return self.seg[i]                               # pachi ye value([low - high] node ki value (sum of arr[low:high + 1])) ko return kar dia for further segment sum
        
    def update(self, arr, idx, val, i=0, low=0, high=None):      # i = index of the current node
        if high is None:
            high = self.n - 1
            
        if low == high:                                 # ith node shows the range sum from arr[low, high]
            self.seg[i] = val
            return 
        
        mid = (low + high)//2
        
        if idx <= mid:
            self.update(arr, idx, val, 2*i + 1, low, mid)
        else:
            self.update(arr, idx, val, 2*i + 2, mid + 1, high)
            
        self.seg[i] = self.seg[2*i + 1] + self.seg[2*i + 2]

    def query(self, l, r, i=0, low=0, high=None):
        if high is None:
            high = self.n - 1
        
        if r < low or l > high:         # no overlap
            return 0
        elif l <= low and high <= r:    # complete overlap      l...(low....high)...r
            return self.seg[i]
        else:
            mid = (low + high)//2
            
            left = self.query(l, r, 2*i + 1, low, mid)
            right = self.query(l, r, 2*i + 2, mid + 1, high)
            
            return left + right


# Input array
arr = [1, 2, 3, 4, 5]

# Initialize segment tree
n = len(arr)
tree = segtree(n)

# Build the tree
tree.build_tree(arr)

# Update index 2 to 10
tree.update(arr, 2, 10)

# Query range sum from index 1 to 3
print(tree.query(1, 3))  # Output: 16 (2 + 10 + 4)
