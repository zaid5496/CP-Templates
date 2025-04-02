import heapq

def prim(n, adj):
    visited = [False]*(n+1)    # for 1 edged graphs
    min_heap = [(0, 0)]  # (weight, node)..........(0, 1) for 1 - indexed graphs
    mst_weight = 0
    mst_edges = []

    while min_heap:
        w, u = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        mst_weight += w
        for v, weight in adj[u]:  # Iterate through neighbors
            if not visited[v]:
                heapq.heappush(min_heap, (weight, v))
                mst_edges.append((u, v, weight))

    return mst_weight, mst_edges

# Example Usage
n = 4
adj_list = {
    0: [(1, 10), (2, 5), (3, 6)],
    1: [(0, 10), (2, 15)],
    2: [(0, 5), (1, 15), (3, 4)],
    3: [(0, 6), (2, 4)]
}
print(prim(n, adj_list))
