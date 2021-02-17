# 3
# 3
# 5 5 4
# 3 9 1
# 3 2 7
# 5
# 3 7 2 0 1
# 2 8 0 9 1
# 1 2 1 8 1
# 9 8 9 2 0
# 3 6 5 1 5
# 7
# 9 0 5 1 1 5 3
# 4 1 2 1 6 5 3
# 0 7 6 1 6 8 5
# 1 1 7 8 3 2 3
# 9 4 0 7 6 4 1
# 5 8 3 2 4 8 3
# 7 4 8 4 8 3 4

import heapq

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
t = int(input())

for _ in range(t):
    n = int(input())
    INF = n * n * 9 + 1
    g = []
    d = [[INF] * n for _ in range(n)]
    for i in range(n):
        g.append(list(map(int, input().split())))

    q = []
    heapq.heappush(q, (g[0][0], 0, 0))
    while q:
        cost, y, x = heapq.heappop(q)

        if cost >= d[y][x]:
            continue

        d[y][x] = cost

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                ncost = cost + g[ny][nx]
                if ncost < d[ny][nx]:
                    heapq.heappush(q, (ncost, ny, nx))

    print(d[n-1][n-1])
