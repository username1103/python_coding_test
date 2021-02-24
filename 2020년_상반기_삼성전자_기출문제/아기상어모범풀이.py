from collections import deque
INF = 1e9

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

n = int(input())

g = []
for i in range(n):
    g.append(list(map(int, input().split())))

shark_size = 2
shark_y, shark_x = 0, 0

for i in range(n):
    for j in range(n):
        if g[i][j] == 9:
            shark_y, shark_x = i, j
            g[shark_y][shark_x] = 0


# 상어의 위치부터 모든 장소까지 거리를 갱신
def bfs(g, shark_y, shark_x, shark_size):
    length_from_shark = [[-1] * n for _ in range(n)]
    q = deque([(shark_y, shark_x)])
    length_from_shark[shark_y][shark_x] = 0

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                if length_from_shark[ny][nx] == -1 and g[ny][nx] <= shark_size:
                    length_from_shark[ny][nx] = length_from_shark[y][x] + 1
                    q.append((ny, nx))

    return length_from_shark


# 가장 가까운 상어위치 반환
def find(g, length_from_shark, shark_size):
    y, x = 0, 0
    min_length = INF
    for i in range(n):
        for j in range(n):
            # 도달 가능하고, 상어보다 작으면
            if length_from_shark[i][j] != -1 and 1 <= g[i][j] < shark_size:
                if length_from_shark[i][j] < min_length:
                    y, x = i, j
                    min_length = length_from_shark[i][j]

    if min_length == INF:
        return None
    else:
        return y, x, min_length


result = 0  # 총 시간
ate = 0  # 먹은 물고기 수

while True:
    value = find(g, bfs(g, shark_y, shark_x, shark_size), shark_size)

    # 먹을 수 있는 물고기가 없다면
    if value == None:
        print(result)
        break
    # 먹을 수 있는 물고기가 있다면
    else:
        shark_y, shark_x = value[0], value[1]
        result += value[2]
        g[shark_y][shark_x] = 0
        ate += 1

        if ate >= shark_size:
            shark_size += 1
            ate = 0
