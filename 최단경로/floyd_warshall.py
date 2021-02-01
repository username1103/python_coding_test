# 4
# 7
# 1 2 4
# 1 4 6
# 2 1 3
# 2 3 7
# 3 1 5
# 3 4 4
# 4 3 2

INF = int(1e9)

n = int(input())
m = int(input())

# 2차원 배열 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 대각선 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 현재 연결되어 있는 부분 초기화
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 모든 경우의 수에 대해서 최소 값으로 갱신
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# print
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print("INFINITY", end=" ")
        else:
            print(graph[a][b], end=" ")
    print()
