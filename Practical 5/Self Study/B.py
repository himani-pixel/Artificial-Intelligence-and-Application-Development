from collections import deque

maze = [
    ['S', '.', '.', '#'],
    ['#', '.', '#', '.'],
    ['.', '.', '.', '.'],
    ['#', '#', '.', 'G']
]

rows, cols = len(maze), len(maze[0])

# Find Start and Goal positions
for i in range(rows):
    for j in range(cols):
        if maze[i][j] == 'S':
            start = (i, j)
        if maze[i][j] == 'G':
            goal = (i, j)

queue = deque([(start, [start])])
visited = {start}

while queue:
    (x, y), path = queue.popleft()

    if (x, y) == goal:
        print("Shortest Path:", path)
        break

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy

        if (
            0 <= nx < rows and
            0 <= ny < cols and
            maze[nx][ny] != '#' and
            (nx, ny) not in visited
        ):
            visited.add((nx, ny))
            queue.append(((nx, ny), path + [(nx, ny)]))

print("Himani T016")
