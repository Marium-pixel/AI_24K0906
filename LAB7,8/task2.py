#task2:
visited_ab = []
pruned_nodes = []

def alpha_beta(node, depth, alpha, beta, maximizingPlayer):
    visited_ab.append(node.name)

    if not node.children or depth == 0:
        return node.value

    if maximizingPlayer:
        value = float('-inf')
        for child in node.children:
            value = max(value, alpha_beta(child, depth-1, alpha, beta, False))
            alpha = max(alpha, value)
            if beta <= alpha:
                pruned_nodes.append(child.name)
                break
        node.value = value
        return value
    else:
        value = float('inf')
        for child in node.children:
            value = min(value, alpha_beta(child, depth-1, alpha, beta, True))
            beta = min(beta, value)
            if beta <= alpha:
                pruned_nodes.append(child.name)
                break
        node.value = value
        return value


visited_ab.clear()
pruned_nodes.clear()

print("\nAlpha-Beta Value:", alpha_beta(root, 10, float('-inf'), float('inf'), True))
print("Visited:", visited_ab)
print("Pruned:", pruned_nodes)
