import heapq

def dijkstra(g, s):                   # (adjacency list, source)
    d = {n: float('inf') for n in g}  # dictionary which stores the shortest path from source to every node
    d[s] = 0                          # dist of source from source(itself) is 0
    pq = [(0, s)]                     # (distance, node)..........heap me daal dia
    
    while pq:
        cd, cn = heapq.heappop(pq)    # sabse close(kareeb) neighbor with the least distance
        
        if cd > d[cn]:                # iska mtlb ki heap me ek point pe jab humne ek x node ka distance push kia tha
            continue                  # vo aage jaake algo ki madad se aur kam ho gya to ab purane cd ko leke koi fayda nai he so we'll skip this node
                                      # usually to avoid cycle back to the source
        
        for n, w in g[cn]:
            dist = cd + w
            
            if dist < d[n]:
                d[n] = dist
                heapq.heappush(pq, (dist, n))
    
    return d

# Example usage:
g = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

s = 'A'
shortest_paths = dijkstra(g, s)
print(shortest_paths)



# https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/
# https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/