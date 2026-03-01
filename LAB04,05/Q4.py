import heapq

graph = {
    'S': {'A': 4, 'B': 2},
    'A': {'C': 5, 'D': 10},
    'B': {'E': 3},
    'C': {'G': 4},
    'D': {'G': 1},
    'E': {'D': 4},
    'G': {}
}

def ucs(start, goal):
    frontier = []
    heapq.heappush(frontier, (0, start, [start]))
    explored = set()

    while frontier:
        cost, node, path = heapq.heappop(frontier)
        if node == goal:
            return path, cost
        if node not in explored:
            explored.add(node)
            for neighbor, weight in graph[node].items():
                if neighbor not in explored:
                    heapq.heappush(frontier, (cost + weight, neighbor, path + [neighbor]))
    return None, float('inf')

start = 'S'
goal = 'G'
path, total_cost = ucs(start, goal)
print("Least Cost Path:", path)
print("Total Cost:", total_cost)
