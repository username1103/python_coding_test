# 7 11
# 0 1 7
# 0 3 5
# 1 2 8
# 1 3 9
# 1 4 7
# 2 4 5
# 3 4 15
# 3 5 6
# 4 5 8
# 4 6 9
# 5 6 11

# 51

import heapq


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y


n, m = map(int, input().split())

parent = [i for i in range(n)]
q = []

total = 0
for _ in range(m):
    x, y, cost = map(int, input().split())
    heapq.heappush(q, (cost, x, y))
    total += cost

use_cost = 0
while q:
    cost, x, y = heapq.heappop(q)
    x = find_parent(parent, x)
    y = find_parent(parent, y)

    if x != y:
        union(parent, x, y)
        use_cost += cost

print(total - use_cost)
