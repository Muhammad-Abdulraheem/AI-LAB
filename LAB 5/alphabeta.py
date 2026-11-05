ab_leaf_count = 0

def alphabeta(depth, node_index, is_max_turn, scores, target_depth, alpha, beta):
    global ab_leaf_count
    if depth == target_depth:
        ab_leaf_count += 1
        return scores[node_index]
    
    if is_max_turn:
        value = float('-inf')
        for i in range(2):
            val = alphabeta(depth + 1, node_index * 2 + i, False, scores, target_depth, alpha, beta)
            value = max(value, val)
            alpha = max(alpha, value)
            if alpha >= beta:
                break 
        return value
    else:
        value = float('inf')
        for i in range(2):
            val = alphabeta(depth + 1, node_index * 2 + i, True, scores, target_depth, alpha, beta)
            value = min(value, val)
            beta = min(beta, value)
            if alpha >= beta:
                break 
        return value

scores = [3, 5, 2, 9, 3, 5, 2, 9]
depth = 3

print("Alpha-beta")
print("Optimal Value:", alphabeta(0, 0, True, scores, depth, float('-inf'), float('inf')))
print("Leave check:", ab_leaf_count)