graph = {"A": ["B","C"], "B": ["D","E"], "C": ["F"],
         "D": [], "E": ["G"], "F": [], "G": []}

def dls(start, goal, limit):
    stack = [(start, [start])]
    cutoff = False
    while stack:
        node, path = stack.pop()
        if node == goal:
            return "Found", path
        if len(path) - 1 == limit:
            if graph[node]:
                cutoff = True
            continue
        for n in reversed(graph[node]):
            if n not in path:
                stack.append((n, path + [n]))
    if cutoff:
        return "cut", None
    return "fail", None
for L in [1, 2, 3, 4]:
    status, path = dls("A", "G", L)

print(f"limit={L}: {status}" + (f", path={path}" if path else ""))
