# 5
# 10 -1
# 10 1 -1
# 4 1 -1
# 4 3 1 -1
# 3 3 -1
from collections import deque
import copy

n = int(input())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
time = [0] * (n + 1)

for i in range(1, n + 1):
    temp = list(map(int, input().split()))
    time[i] = temp[0]
    for x in temp[1:-1]:
        indegree[i] += 1
        graph[x].append(i)


def topology_sort():
    result = copy.deepcopy(time)
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        temp = q.popleft()
        for x in graph[temp]:
            result[x] = max(result[x], result[temp] + result[x])
            indegree[x] -= 1
            if indegree[x] == 0:
                q.append(x)

    for i in range(1, n + 1):
        print(result[i])


topology_sort()
