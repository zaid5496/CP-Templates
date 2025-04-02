import heapq

def prim(start, graph):
    n = len(graph)
    mst_edge = [[] for _ in range(n+1)]
    total_weight = 0
    visited = set([start])
    pq = []
    
    for v, wt in graph[start]:
        heapq.heappush(pq, (wt, start, v))
    
    while pq and len(visited) < n:
        wt, u, v = heapq.heappop(pq)
        if v in visited:
            continue
        visited.add(v)
        total_weight += wt
        mst_edge[u].append((v, wt))
        mst_edge[v].append((u, wt))
        
        for w, wt_next in graph[v]:
            if w not in visited:
                heapq.heappush(pq, (wt_next, v, w))
                
    
    return total_weight, mst_edge

if __name__ == '__main__':
    graph = {
        0: [(1, 4), (7, 8)],
        1: [(0, 4), (2, 8), (7, 11)],
        2: [(1, 8), (3, 7), (5, 4), (8, 2)],
        3: [(2, 7), (4, 9), (5, 14)],
        4: [(3, 9), (5, 10)],
        5: [(2, 4), (3, 14), (4, 10), (6, 2)],
        6: [(5, 2), (7, 1), (8, 6)],
        7: [(0, 8), (1, 11), (6, 1), (8, 7)],
        8: [(2, 2), (6, 6), (7, 7)]
    }
    
    total, mst_edge = prim_mst(graph, start=0)
    print("Total weight of MST:", total)
    print("MST adjacency list:")
    for u in mst_edge:
        print(f"{u}: {mst_edge[u]}")
