import copy

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

graph = [[] for _ in range(4)]
for i in range(4):
    temp = list(map(int, input().split()))
    for j in range(0, 8, 2):
        graph[i].append([temp[j], temp[j + 1] - 1])

max_value = 0


def moveFish(graph, now_y, now_x):
    for i in range(1, 17):
        pos = findFish(graph, i)
        if pos != None:
            y, x = pos[0], pos[1]
            d = graph[y][x][1]
            for j in range(8):
                ny = y + dy[d]
                nx = x + dx[d]
                if 0 <= ny < 4 and 0 <= nx < 4:
                    if not (nx == now_x and ny == now_y):
                        graph[y][x][1] = d
                        graph[y][x], graph[ny][nx] = graph[ny][nx], graph[y][x]
                        break
                d = (d + 1) % 8


def findFish(graph, num):
    for i in range(4):
        for j in range(4):
            if graph[i][j][0] == num:
                return (i, j)
    return None


def get_possible_shark_pos(graph, y, x):
    pos = []
    d = graph[y][x][1]
    for i in range(4):
        x += dx[d]
        y += dy[d]
        if 0 <= x < 4 and 0 <= y < 4:
            if graph[y][x][0] != -1:
                pos.append((y, x))
    return pos


def dfs(graph, y, x, total):
    global max_value
    graph = copy.deepcopy(graph)

    total += graph[y][x][0]
    graph[y][x][0] = -1

    moveFish(graph, y, x)

    pos = get_possible_shark_pos(graph, y, x)
    if len(pos) == 0:
        max_value = max(max_value, total)
        return

    for y, x in pos:
        dfs(graph, y, x, total)


dfs(graph, 0, 0, 0)
print(max_value)
