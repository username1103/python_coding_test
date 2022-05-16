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
        parent[x] = find_parent(parent, parent[x])  # path compression 이용
        return parent[x]
    return x


def union(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


# 집의 수와 길의 수
n, m = map(int, input().split())

q = []
parent = [i for i in range(n + 1)]  # rank는 이용 x

# 비용에 따른 오름차순 정렬을 위해 heapq 이용
for i in range(m):
    a, b, cost = map(int, input().split())
    heapq.heappush(q, (cost, a, b))

total = 0  # 총 비용
big = 0  # 가장 비용이 큰 길

# 크루스칼 알고리즘 수행
while q:
    cost, a, b = heapq.heappop(q)

    if find_parent(parent, a) != find_parent(parent, b):
        union(parent, a, b)
        total += cost
        big = cost

# 전체 최소 스패닝 트리에서 비용이 가장 큰 길을 제거 하여 두 개의 마을로 분리
print(total - big)
