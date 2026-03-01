from collections import deque

building = [
    [1, 1, 0, 1],
    [0, 1, 1, 1],
    [1, 1, 0, 1],
    [1, 0, 1, 1]
]

rows, cols = len(building), len(building[0])
directions = [(-1,0), (1,0), (0,-1), (0,1)]

graph = {}
for r in range(rows):
    for c in range(cols):
        if building[r][c] == 1:
            neighbors = []
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and building[nr][nc] == 1:
                    neighbors.append((nr, nc))
            graph[(r, c)] = neighbors

def bfs(start, goal, graph):
    visited = set()
    queue = deque([start])
    parent = {start: None}
    traversal_order = []

    while queue:
        node = queue.popleft()
        traversal_order.append(node)
        if node == goal:
            break
        for neighbor in graph.get(node, []):
            if neighbor not in visited and neighbor not in queue:
                queue.append(neighbor)
                parent[neighbor] = node
        visited.add(node)

    path = []
    if goal in parent:
        current = goal
        while current is not None:
            path.append(current)
            current = parent[current]
        path.reverse()

    return traversal_order, path

start = (0,0)
goal = (3,3)
traversal_order, shortest_path = bfs(start, goal, graph)

print("BFS Traversal Order:")
print(traversal_order)
print("Shortest Path from Start to Emergency Exit:")
print(shortest_path)
