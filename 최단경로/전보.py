# 3 2 1
# 1 2 4
# 1 3 2

import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, m, start = map(int, input().split())  # 도시 수, 통로 수, 시작 도시
graph = [[] for i in range(n + 1)]  # 인접 리스트를 통한 간선 관리
distance = [INF] * (n + 1)  # 다익스트라를 위한 테이블 초기화

# 각각의 간선들의 정보를 인접리스트에 저장
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))


# 다익스트라 알고리즘
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

count = 0  # 연결된 도시의 수
max_distance = 0  # 가장 멀리 있는 도시와 거리
for d in distance:
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

print(count - 1, max_distance)
