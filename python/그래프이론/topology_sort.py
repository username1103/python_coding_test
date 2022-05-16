# 7 8
# 1 2
# 1 5
# 2 3
# 2 6
# 3 4
# 4 7
# 5 6
# 6 4

from collections import deque

v, e = map(int, input().split())

indegree = [0] * (v + 1)  # 각 노드의 차수 저장

graph = [[] for i in range(v + 1)]  # 인접 리스트로 연결 관리

for i in range(e):
    start, end = map(int, input().split())
    graph[start].append(end)
    indegree[end] += 1


# 큐에서 꺼내어 해당 원소랑 연결된 간선들 제거해주며 차수가 0인 노드를 큐에 삽입
# 만약 모든 노드를 방문하기 전에 큐가 빌 경우, 사이클이 존재함을 의미
def topology_sort():
    result = []
    q = deque()
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        temp = q.popleft()
        result.append(temp)
        for end in graph[temp]:
            indegree[end] -= 1
            if indegree[end] == 0:
                q.append(end)

    return result


result = topology_sort()

for i in result:
    print(i, end=" ")
