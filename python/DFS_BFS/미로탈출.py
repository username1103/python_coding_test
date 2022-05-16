# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111

from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

start = [0, 0]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(start):
    q = deque()
    q.append((start[0], start[1]))
    while q:
        y, x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue

            if graph[ny][nx] == 0:
                continue

            if graph[ny][nx] == 1:
                graph[ny][nx] = graph[y][x] + 1
                q.append((ny, nx))

    return graph[n-1][m-1]


print(bfs(start))
