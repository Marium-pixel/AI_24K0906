# Modify leaves
leaves_mod = [Node(str(v), value=v) for v in [10,3,6,9,2,14,5,1]]

N3 = Node("N3", [leaves_mod[0], leaves_mod[1]])
N4 = Node("N4", [leaves_mod[2], leaves_mod[3]])
N5 = Node("N5", [leaves_mod[4], leaves_mod[5]])
N6 = Node("N6", [leaves_mod[6], leaves_mod[7]])

N1 = Node("N1", [N3, N4])
N2 = Node("N2", [N5, N6])

root_mod = Node("Root", [N1, N2])

# Run
visited_ab.clear()
pruned_nodes.clear()

val = alpha_beta(root_mod, 10, float('-inf'), float('inf'), True)
print("\nModified Tree Value:", val)
print("Pruned Nodes:", pruned_nodes)

# Optimal path
def get_path(node, maximizing):
    if not node.children:
        return [node.name]

    best_child = None
    if maximizing:
        best_val = float('-inf')
        for c in node.children:
            if c.value > best_val:
                best_val = c.value
                best_child = c
    else:
        best_val = float('inf')
        for c in node.children:
            if c.value < best_val:
                best_val = c.value
                best_child = c

    return [node.name] + get_path(best_child, not maximizing)

print("Optimal Path:", get_path(root_mod, True))
