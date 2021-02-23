from collections import deque


def bfs(graph, shark, can_eat_fish):
    out = [[-1] * n for _ in range(n)]
    out[shark[1]][shark[2]] = 0
    q = deque()
    q.append((shark[1], shark[2]))
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < n and graph[ny][nx] <= shark_size and out[ny][nx] == -1:
                out[ny][nx] = out[y][x] + 1
                q.append((ny, nx))

    min_value = 401
    min_fish = []
    for fish in can_eat_fish:
        if out[fish[1]][fish[2]] < min_value:
            min_value = out[fish[1]][fish[2]]
            min_fish = fish

    return min_value, min_fish


dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

n = int(input())
graph = []

shark = []
shark_size = 2
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] == 9:
            shark = [shark_size, i, j]

fishes = []
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0 and graph[i][j] != 9:
            fishes.append((graph[i][j], i, j))


time = 0
can_eat_fish = [fish for fish in fishes if fish[0] < shark_size]

ate = 0
while len(can_eat_fish) != 0:
    length, min_fish = bfs(graph, shark, can_eat_fish)

    if min_fish == []:
        break

    time += length
    ate += 1
    if shark_size == ate:
        shark_size += 1
        ate = 0
    graph[shark[1]][shark[2]] = 0
    shark = [shark_size, min_fish[1], min_fish[2]]
    graph[min_fish[1]][min_fish[2]] = 9
    fishes.remove((min_fish[0], min_fish[1], min_fish[2]))

    can_eat_fish = [fish for fish in fishes if fish[0] < shark_size]


print(time)
