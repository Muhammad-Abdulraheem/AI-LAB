leaf_count = 0

def minimax(depth, node_index, is_max_turn, scores, target_depth):
    global leaf_count
    if depth == target_depth:
        leaf_count += 1
        return scores[node_index]
    
    if is_max_turn:
        left = minimax(depth + 1, node_index * 2, False, scores, target_depth)
        right = minimax(depth + 1, node_index * 2 + 1, False, scores, target_depth)
        return max(left, right)
    else:
        left = minimax(depth + 1, node_index * 2, True, scores, target_depth)
        right = minimax(depth + 1, node_index * 2 + 1, True, scores, target_depth)
        return min(left, right)
    
scores = [3, 5, 2, 9, 3, 5, 2, 9]
depth = 2

print("Minimax")
print("Value:", minimax(0, 0, True, scores, depth))
print("Leaves checking:", leaf_count)