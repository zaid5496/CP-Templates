import heapq

def dijkstra(g, s):                   # (adjacency list, source)
    n = len(g)
    d = [float('inf')]*(n+1)          # dictionary which stores the shortest path from source to every node
    parent = [-1]*(n+1)               # parent array so we can race back the shortest path
    d[s] = 0                          # dist of source from source(itself) is 0
    pq = [(0, s)]                     # (distance, node)..........heap me daal dia
    
    while pq:
        cd, node = heapq.heappop(pq)    # sabse close(kareeb) neighbor with the least distance
        
        if cd > d[node]:                # iska mtlb ki heap me ek point pe jab humne ek x node ka distance push kia tha
            continue                  # vo aage jaake algo ki madad se aur kam ho gya to ab purane cd ko leke koi fayda nai he so we'll skip this node
                                      # usually to avoid cycle back to the source
        for child, val in g[node]:
            dist = cd + val          
            if dist < d[child]:
                d[child] = dist
                parent[child] = node
                heapq.heappush(pq, (dist, child))        # daal dia isko heap me, so that in future we can reach to this node(maybe:) )
    
    return d, parent

# Example usage:
adj = [[], [(2, 2), (4, 1)], [(1, 2), (5, 5), (3, 4)], [(2, 4), (4, 3), (5, 1)], [(1, 1), (3, 3)], [(2, 5), (3, 1)]]

s = 1
shortest_paths, parent = dijkstra(adj, s)
print(shortest_paths, parent)



# https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/
# https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/
# https://codeforces.com/contest/20/problem/C
