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


# union find 알고리즘
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


# 마을의 수와 집의 수 입력받기
n, m = map(int, input().split())
# 부모테이블 갱신
parent = [i for i in range(n)]
q = []  # 크루스칼 알고리즘을 위한 큐

# 각 길을 비용순으로 heap큐에 저장 & 전체 비용 저장
total = 0
for _ in range(m):
    x, y, cost = map(int, input().split())
    heapq.heappush(q, (cost, x, y))
    total += cost

# 비용이 적은 길부터 뽑아와 길을 연결
use_cost = 0
while q:
    cost, x, y = heapq.heappop(q)
    x = find_parent(parent, x)
    y = find_parent(parent, y)

    # 두 길의 부모가 다르다면, 즉 길이 연결되지 않았다면, 길을 연결하고 해당 비용을 저장
    if x != y:
        union(parent, x, y)
        use_cost += cost

# 전체 비용에서 사용 비용을 제거하여 절약한 비용 출력
print(total - use_cost)
