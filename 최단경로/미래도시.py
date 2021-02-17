# 5 7
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
# 4 5

# 4 2
# 1 3
# 2 4
# 3 4
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())  # 도시의 수와 간선의 수

graph = [[INF] for _ in range(n + 1)]  # 플루이드 와샬 알고리즘을 위한 테이블

# 테이블 초기화
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 경유지와 목적지
x, k = map(int, input().split())

# 자기 자신을 0으로 테이블 초기화
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

# i에서 j로 갈 때, 현재 구해진 값과 k를 경유해서 갈 경우의 값을 비교하여 작은 값으로 갱신
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 최종 거리
distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print("-1")
else:
    print(distance)
