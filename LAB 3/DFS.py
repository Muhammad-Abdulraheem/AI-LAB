from collections import deque
graph = {"A":
         ["B","C"], "B":["D","E"], "C":["F"],
         "D":[], "E":["G"], "F":[], "G":[]}

def dfs(start, goal):
    stack = [(start, [start])]
    seen = set()
    while stack:
        node, path = stack.pop()          
        if node == goal:                  
            return path
        if node in seen:                  
            continue
        seen.add(node)                    
        for n in reversed(graph[node]):   
            stack.append((n, path + [n]))

print(dfs("A", "G"))