from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': ['G'],
}

def dfs(graph, node, visited=None):
    if visited is None:
        visited = []
    
    if node not in visited:
        visited.append(node) 
        
        for adjacent in graph[node]:
            dfs(graph, adjacent, visited)
    return visited

from collections import deque

def bfs(graph, starting_node):
    visited = []
    queue = deque([starting_node])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            
            for adjacent in graph[node]:
                queue.append(adjacent)
    return visited 

print()
print("DFS Traversal: ", dfs(graph, 'A'))
print("BFS Traversal: ", bfs(graph, 'A'))
print()



