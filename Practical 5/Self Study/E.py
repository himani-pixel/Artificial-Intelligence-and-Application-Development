import heapq

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [('G', 4)],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}

h = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 4,
    'E': 2,
    'F': 1,
    'G': 0
}


def search(start, goal, astar=True):
    pq = [(0, start, [start])]
    visited = set()

    while pq:
        cost, node, path = heapq.heappop(pq)

        if node == goal:
            return path, cost

        if node in visited:
            continue

        visited.add(node)

        for nxt, w in graph[node]:
            g = cost - h[node] if astar else cost
            ncost = g + w + (h[nxt] if astar else 0)
            heapq.heappush(pq, (ncost, nxt, path + [nxt]))


ucs_path, ucs_cost = search('A', 'G', False)
astar_path, astar_cost = search('A', 'G', True)

print("UCS Path :", ucs_path, "Cost :", ucs_cost)
print("A* Path  :", astar_path, "Cost :", astar_cost)

print("Himani T016")
