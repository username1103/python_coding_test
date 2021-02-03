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

indegree = [0] * (v + 1)

graph = [[] for i in range(v + 1)]

for i in range(e):
    start, end = map(int, input().split())
    graph[start].append(end)
    indegree[end] += 1


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
