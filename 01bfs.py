from collections import deque

# https://leetcode.com/problems/shortest-bridge/
# https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/
# https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/


# there is no need of visited in 01 bfs
# In 0-1 BFS, we often don’t explicitly need a visited set because the algorithm's structure naturally ensures that no node is revisited unnecessarily. 
# This is due to the properties of the deque and the edge relaxation process. 
# infinite loop pe nai jayega kabhi bhi bcs of this condition:..... if curr_dist < dist[child]
def zero_one_bfs(graph, start):
    n = len(graph)
    dist = [float('inf')] * n
    dist[start] = 0
    q = deque([start])
    
    while q:
        node = q.popleft()
        for child, weight in graph[node]:
            curr_dist = dist[node] + weight
            if curr_dist < dist[child]:
                dist[child] = curr_dist
                if weight == 0:
                    q.appendleft(child)  # Higher priority
                else:
                    q.append(child)  # Lower priority
                    
    return dist

# Example usage:
graph = {
    0: [(1, 0), (2, 1)],
    1: [(3, 1), (4, 0)],
    2: [(5, 1)],
    3: [(5, 0)],
    4: [(5, 1)],
    5: []
}
print(zero_one_bfs(graph, 0))  # Output: [0, 0, 1, 1, 0, 1]
