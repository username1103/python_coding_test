import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)
n, m = map(int, input().rstrip().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

x, k = map(int, input().rstrip().split())

distance = [INF] * (n + 1)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for next in graph[now]:
            cost = dist + 1
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(q, (cost, next))


# 1에서 k까지 거리 찾기
dijkstra(1)
a = distance[k]

# 거리 초기화
distance = [INF] * (n + 1)

# k에서 x까지 거리 찾기
dijkstra(k)
b = distance[x]


if a + b >= INF:
    print(-1)
else:
    print(a + b)
