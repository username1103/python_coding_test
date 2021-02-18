# 7 9
# 1 2 29
# 1 5 75
# 2 3 35
# 2 6 34
# 3 4 7
# 4 6 23
# 4 7 13
# 5 6 53
# 6 7 25

import heapq


def find_parent(parent, x):
    if parent[x][0] != x:
        parent[x][0] = find_parent(parent, parent[x][0])
        return parent[x][0]
    return x


def union(parent, x, y):
    x_root = find_parent(parent, x)
    y_root = find_parent(parent, y)

    if parent[x_root][1] == parent[y_root][1]:
        parent[x_root][1] += 1
        parent[y_root][0] = x_root
    elif parent[x_root][1] < parent[y_root][1]:
        parent[x_root][0] = y_root
    else:
        parent[y_root][0] = x_root


v, e = map(int, input().split())

parent = [[0] * 2 for _ in range(v + 1)]
for i in range(1, v + 1):
    parent[i][0] = i
    parent[i][1] = 1

q = []

for i in range(e):
    x, y, cost = map(int, input().split())
    heapq.heappush(q, (cost, x, y))

total_cost = 0
while q:
    cost, v1, v2 = heapq.heappop(q)
    v1_parent = find_parent(parent, v1)
    v2_parent = find_parent(parent, v2)

    # 싸이클이 발생하지 않으면 트리에 포함 시킴
    # 부모가 같다는 건 사이클이 발생했다는 것을 의미
    if v1_parent != v2_parent:
        union(parent, v1, v2)
        total_cost += cost

print(total_cost)
