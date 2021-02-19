from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):

    n = int(input())

    last_year = list(map(int, input().split()))
    indegree = [0] * (n + 1)

    graph = [[] for _ in range(n + 1)]
    for i in range(n):
        for j in range(i+1, n, 1):
            graph[last_year[i]].append(last_year[j])
            indegree[last_year[j]] += 1

    m = int(input())

    for _ in range(m):
        a, b = map(int, input().split())
        if a in graph[b]:
            graph[a].append(b)
            indegree[b] += 1
            indegree[a] -= 1
            if a in graph[b]:
                graph[b].remove(a)
        else:
            graph[b].append(a)
            indegree[a] += 1
            indegree[b] -= 1
            if b in graph[a]:
                graph[a].remove(b)

    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    result = []
    certain = True
    isImpossible = False
    for i in range(n):
        if len(q) == 0:
            isImpossible = True
            break
        if len(q) == 1:
            now = q.pop()
            result.append(now)
            for node in graph[now]:
                indegree[node] -= 1
                if indegree[node] == 0:
                    q.appendleft(node)
        else:
            certain = False
            break

    if isImpossible:
        print("IMPOSSIBLE")
    elif certain:
        for i in result:
            print(i, end=" ")
        print()
    else:
        print('?')
