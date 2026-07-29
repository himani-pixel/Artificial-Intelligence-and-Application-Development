from collections import deque

start = (3, 3, 1)
goal = (0, 0, 0)


def valid(s):
    m, c, _ = s
    return (m == 0 or m >= c) and (3 - m == 0 or 3 - m >= 3 - c)


moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

queue = deque([(start, [start])])
visited = {start}

while queue:
    (m, c, b), path = queue.popleft()

    if (m, c, b) == goal:
        print("Solution Path:")
        for p in path:
            print(p)
        break

    for dm, dc in moves:
        if b:
            ns = (m - dm, c - dc, 0)
        else:
            ns = (m + dm, c + dc, 1)

        if (
            0 <= ns[0] <= 3 and
            0 <= ns[1] <= 3 and
            valid(ns) and
            ns not in visited
        ):
            visited.add(ns)
            queue.append((ns, path + [ns]))

print("Himani T016")
