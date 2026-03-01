graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': [],
    'F': ['H'],
    'G': [],
    'H': []
}

def dls(node, goal, limit, path=None, visited=None):
    if path is None:
        path = []
    if visited is None:
        visited = []
    path.append(node)
    visited.append(node)
    if node == goal:
        return True, path, visited
    if limit <= 0:
        path.pop()
        return False, path, visited
    for neighbor in graph.get(node, []):
        found, result_path, result_visited = dls(neighbor, goal, limit-1, path, visited)
        if found:
            return True, result_path, result_visited
    path.pop()
    return False, path, visited

start = 'A'
goal = 'H'

found2, path2, visited2 = dls(start, goal, 2)
print("Depth = 2")
print("Nodes Visited:", visited2)
print("Path Found:", path2 if found2 else "Not Found")

found3, path3, visited3 = dls(start, goal, 3)
print("\nDepth = 3")
print("Nodes Visited:", visited3)
print("Path Found:", path3 if found3 else "Not Found")
