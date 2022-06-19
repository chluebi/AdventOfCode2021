import copy

with open('input') as f:
    s = f.read().strip().split('\n')

vertices = []
edges = {}
for line in s:
    v, u = line.split('-')
    if v not in edges:
        edges[v] = []
        vertices.append(v)
    if u not in edges:
        edges[u] = []
        vertices.append(u)
    
    edges[v].append(u)
    edges[u].append(v)

visited = {v: False for v in vertices}
print(vertices)
print(edges)

count = 0
def dfs(v, visited, twice):
    global count
    visited = copy.deepcopy(visited)
    visited[v] = True
    for edge in edges[v]:
        if edge == 'end':
            count += 1
        elif edge.isupper():
            dfs(edge, visited, twice)
        elif not visited[edge]:
            dfs(edge, visited, twice)
        elif not twice and edge not in ['start', 'end']:
            dfs(edge, visited, True)
        
dfs('start', visited, False)
print(count)