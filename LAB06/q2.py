#q.2:
import heapq

goal = 20
 
def heuristic(n):
    return abs(goal - n)
 
def generate_successors(x):
    return [x + 2, x + 3, x * 2]
 
def beam_search(start, goal, beam_width=2):

    beam = [(heuristic(start), [start])]   
    level = 0

    while beam:
        print(f"Level {level} explored:", [path[-1] for _, path in beam])

        candidates = []

        for cost, path in beam:
            current = path[-1]

            if current == goal:
                return path

            for neighbor in generate_successors(current):

                if neighbor <= goal:   
                    new_path = path + [neighbor]
                    new_cost = heuristic(neighbor)
                    candidates.append((new_cost, new_path))

        
        beam = heapq.nsmallest(beam_width, candidates, key=lambda x: x[0])

        level += 1

    return None


 
start_node = 1
goal_node = 20
beam_width = 2

path = beam_search(start_node, goal_node, beam_width)

 
if path:
    print("Final path to reach 20:", " → ".join(map(str, path)))
else:
    print("No path found")
