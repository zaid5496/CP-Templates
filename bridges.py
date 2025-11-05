'''
solved:
    https://codeforces.com/problemset/problem/1986/F
    https://codeforces.com/problemset/problem/118/E
    https://codeforces.com/problemset/problem/1000/E
    https://codeforces.com/problemset/problem/1325/F
    https://codeforces.com/problemset/problem/1364/D

to solve:
    https://codeforces.com/contest/1277/problem/E
    https://codeforces.com/contest/231/problem/E
    https://codeforces.com/contest/732/problem/F
    https://codeforces.com/contest/962/problem/F
    https://codeforces.com/contest/19/problem/E

'''


from types import GeneratorType
 
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:           
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc



def BRIDGE():
    tin = [-1]*(n+1)        # earliest discovery time
    low = [-1]*(n+1)        # the minimum tin of any node we can reach
    visited = [False]*(n+1)
    timer = 0
    
    bridges = []
    
    
    @bootstrap
    def dfs(node, parent):
        global timer
        tin[node] = low[node] = timer
        timer += 1
        visited[node] = True
    
        
        for child in adj[node]:
            if child == parent:
                continue
    
            if not visited[child]:
                yield dfs(child, node)
                
                low[node] = min(low[node], low[child])
                if low[child] > tin[node]:
                    bridges.append((node, child))
                    
            else:
                low[node] = min(low[node], tin[child])
        
        
        yield
        
    dfs(1, -1)

    return bridges
