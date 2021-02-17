# 6 6
# 1 5
# 3 4
# 4 2
# 4 6
# 5 2
# 5 4

n, m = map(int, input().split())
INF = 500 * 500 + 1

data = [[INF] * n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    data[a - 1][b - 1] = 1

for i in range(n):
    data[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            data[i][j] = min(data[i][j], data[i][k] + data[k][j])

result = 0
for i in range(n):
    cnt = 0
    for j in range(n):
        if data[i][j] != INF or data[j][i] != INF:
            cnt += 1
    if cnt == n:
        result += 1

print(result)
