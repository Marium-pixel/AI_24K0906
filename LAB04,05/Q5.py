import heapq

graph = {
    'S': [('A', 3), ('B', 6), ('C', 5)],
    'A': [('D', 9), ('E', 8)],
    'B': [('F', 12), ('G', 14)],
    'C': [('H', 7)],
    'H': [('I', 5), ('J', 6)],
    'I': [('K', 1), ('L', 10), ('M', 2)],
    'D': [], 'E': [],
    'F': [], 'G': [],
    'J': [], 'K': [], 'L': [], 'M': []
}

goals = ['J', 'K']  # based on image

def best_first_multiple_goals(start, goals, graph):
    current = start
    path = [current]
    unvisited_goals = set(goals)
    total_cost = 0

    while unvisited_goals:
        frontier = []
        for neighbor, cost in graph.get(current, []):
            heapq.heappush(frontier, (cost, neighbor, cost))
        found = False
        while frontier:
            _, next_node, edge_cost = heapq.heappop(frontier)
            if next_node in unvisited_goals:
                path.append(next_node)
                total_cost += edge_cost
                current = next_node
                unvisited_goals.remove(next_node)
                found = True
                break
        if not found:
            if frontier:
                _, next_node, edge_cost = heapq.heappop(frontier)
                path.append(next_node)
                total_cost += edge_cost
                current = next_node
            else:
                break
    return path, total_cost

start = 'S'
path, cost = best_first_multiple_goals(start, goals, graph)
print("Path visiting all goals:", path)
print("Total Cost:", cost)
