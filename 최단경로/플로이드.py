import sys
input = sys.stdin.readline

INF = 1000000001
n = int(input())

m = int(input())

out = [[INF] * n for _ in range(n)]
for i in range(n):
    out[i][i] = 0


for _ in range(m):
    x, y, z = map(int, input().split())
    out[x - 1][y - 1] = min(z, out[x - 1][y - 1])

for k in range(n):
    for i in range(n):
        for j in range(n):
            out[i][j] = min(out[i][j], out[i][k] + out[k][j])

for i in range(n):
    for j in range(n):
        if out[i][j] == INF:
            print(0, end=" ")
        else:
            print(out[i][j], end=" ")
    print()
