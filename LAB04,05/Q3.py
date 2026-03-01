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

def ids(start, goal, max_depth):
    for depth in range(max_depth+1):
        visited = []
        found, path, visited_nodes = dls(start, goal, depth, path=[], visited=visited)
        print(f"\nDepth Limit = {depth}")
        print("Nodes Visited:", visited_nodes)
        if found:
            print("Goal Found! Path:", path)
            return path
    print("Goal not found within max depth.")
    return None

start = 'A'
goal = 'G'
max_depth = 5
final_path = ids(start, goal, max_depth)
