# 6 6
# 1 5
# 3 4
# 4 2
# 4 6
# 5 2
# 5 4

import sys
input = sys.stdin.readline


n, m = map(int, input().rstrip().split())

graph = [[0]*n for _ in range(n)]  # 전체 그래프 초기화

for _ in range(m):
    # a가 b보다 작으면 graph[a-1][b-1] = 1, 따라서 b는 a보다 크므로 graph[b-1][a-1] = -1
    a, b = map(int, input().rstrip().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = -1


for k in range(n):
    for i in range(n):
        for j in range(n):
            # i가 k보다 작고 k가 j보다 작으면 i는 j보다 작음을 의미
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1
                graph[j][i] = -1

result = 0
for i in range(n):
    # 0의 개수가 1이면, 즉 i는 다른 모든 숫자와 크고 작음을 비교할 수 있다는 말
    if graph[i].count(0) == 1:
        result += 1

print(result)
