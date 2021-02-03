# 7 12
# 1 2 3
# 1 3 2
# 3 2 1
# 2 5 2
# 3 4 4
# 7 3 6
# 5 1 5
# 1 6 2
# 6 4 1
# 6 5 3
# 4 5 3
# 6 7 4

import heapq


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
        return parent[x]
    return x


def union(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


n, m = map(int, input().split())

q = []
parent = [i for i in range(n + 1)]
for i in range(m):
    a, b, cost = map(int, input().split())
    heapq.heappush(q, (cost, a, b))

total = 0
big = 0

while q:
    cost, a, b = heapq.heappop(q)

    if find_parent(parent, a) != find_parent(parent, b):
        union(parent, a, b)
        total += cost
        big = cost

print(total - big)
