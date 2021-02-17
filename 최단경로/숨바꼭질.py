# 6 7
# 3 6
# 4 3
# 3 2
# 1 3
# 1 2
# 2 4
# 5 2


import heapq

n, m = map(int, input().split())
INF = 20001
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

d = [INF] * n

q = []
heapq.heappush(q, (0, 0))

max_value = 0
max_index = -1
count = 1
while q:
    cost, now = heapq.heappop(q)

    if cost > d[now]:
        continue

    d[now] = cost

    for node in graph[now]:
        ncost = cost + 1
        if ncost < d[node]:
            heapq.heappush(q, (ncost, node))

max_value = 0
max_index = 0
count = 0

for i in range(n):
    if max_value < d[i]:
        max_index = i + 1
        max_value = d[i]
        count = 1
    elif max_value == d[i]:
        count += 1

print(max_index, max_value, count)
