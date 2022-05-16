# 15 14
# 00000111100000
# 11111101111110
# 11011101101110
# 11011101100000
# 11011111111111
# 11011111111100
# 11000000011111
# 01111111111111
# 00000000011111
# 01111111111000
# 00011111111000
# 00000001111000
# 11111111110011
# 11100011111111
# 11100011111111

# 8

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

lrud = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def dfs(y, x):
    if x <= -1 or x >= m or y <= -1 or y >= n:
        return False

    if graph[y][x] == 0:
        graph[y][x] = 1
        dfs(y-1, x)
        dfs(y + 1, x)
        dfs(y, x-1)
        dfs(y, x+1)
        return True

    return False


result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0 and dfs(i, j) == True:
            result += 1

print(result)
