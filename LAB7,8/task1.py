#TASK1:
class Node:
    def __init__(self, name, children=None, value=None):
        self.name = name
        self.children = children or []
        self.value = value

visited_order = []

def minimax(node, depth, maximizingPlayer):
    visited_order.append(node.name)

    # Leaf node
    if not node.children or depth == 0:
        return node.value

    if maximizingPlayer:
        max_eval = float('-inf')
        for child in node.children:
            eval = minimax(child, depth - 1, False)
            max_eval = max(max_eval, eval)
        node.value = max_eval
        return max_eval
    else:
        min_eval = float('inf')
        for child in node.children:
            eval = minimax(child, depth - 1, True)
            min_eval = min(min_eval, eval)
        node.value = min_eval
        return min_eval

 
leaves = [Node(str(v), value=v) for v in [4,7,2,5,1,8,3,6]]

N3 = Node("N3", [leaves[0], leaves[1]])
N4 = Node("N4", [leaves[2], leaves[3]])
N5 = Node("N5", [leaves[4], leaves[5]])
N6 = Node("N6", [leaves[6], leaves[7]])

N1 = Node("N1", [N3, N4])
N2 = Node("N2", [N5, N6])

root = Node("Root", [N1, N2])
 
visited_order.clear()
print("Minimax Value:", minimax(root, 10, True))
print("Visited Order:", visited_order)

visited_order.clear()
print("\nDepth-Limited (2):", minimax(root, 2, True))
print("Visited Order:", visited_order)
