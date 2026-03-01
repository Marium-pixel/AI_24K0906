import heapq
import random
import time

graph = {
    'A': {'B': 4, 'C': 3},
    'B': {'E': 12, 'F': 5},
    'C': {'D': 7, 'E': 10},
    'D': {'E': 2},
    'E': {'G': 5},
    'F': {'G': 16},
    'G': {}
}

heuristic = {'A': 14, 'B': 12, 'C': 11, 'D': 6, 'E': 4, 'F': 11, 'G': 0}

def a_star(start, goal, graph, heuristic):
    frontier = []
    heapq.heappush(frontier, (heuristic[start], 0, start, [start]))
    visited_costs = {start: 0}

    while frontier:
        f, cost_so_far, node, path = heapq.heappop(frontier)
        if node == goal:
            return path, cost_so_far

        for neighbor, edge_cost in graph[node].items():
            new_cost = cost_so_far + edge_cost
            if neighbor not in visited_costs or new_cost < visited_costs[neighbor]:
                visited_costs[neighbor] = new_cost
                heapq.heappush(frontier, (new_cost + heuristic[neighbor], new_cost, neighbor, path + [neighbor]))
    return None, float('inf')

def random_update_edge(graph):
    u = random.choice(list(graph.keys()))
    if graph[u]:
        v = random.choice(list(graph[u].keys()))
        old_cost = graph[u][v]
        change = random.randint(-5, 5)
        new_cost = max(1, old_cost + change)
        graph[u][v] = new_cost
        print(f"Edge cost changed: {u} -> {v} from {old_cost} to {new_cost}")

start = 'A'
goal = 'G'

# Simulate dynamic environment
for i in range(5):
    path, cost = a_star(start, goal, graph, heuristic)
    print(f"\nIteration {i+1}:")
    print("Current Optimal Path:", path)
    print("Total Cost:", cost)
    
    # Randomly update one edge cost
    random_update_edge(graph)
    time.sleep(1)  # simulate time passing
