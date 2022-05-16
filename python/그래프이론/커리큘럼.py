# 5
# 10 -1
# 10 1 -1
# 4 1 -1
# 4 3 1 -1
# 3 3 -1
from collections import deque
import copy

n = int(input())  # 듣고자 하는 강의 수
graph = [[] for _ in range(n + 1)]  # 인접리스트
indegree = [0] * (n + 1)  # 각 노드의 차수 테이블
time = [0] * (n + 1)  # 각 노드의 시간 테이블

#
for i in range(1, n + 1):

    temp = list(map(int, input().split()))
    time[i] = temp[0]  # 시간 갱신
    # 꼭 들어야 하는 과목에 따라 해당 노드의 차수 증가
    # 그리고 해당 노드로 들어오도록 간선 추가
    for x in temp[1:-1]:
        indegree[i] += 1
        graph[x].append(i)


def topology_sort():
    result = copy.deepcopy(time)  # 결과를 담을 리스트
    q = deque()

    # 차수가 0인 노드를 큐에 삽입
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        temp = q.popleft()

        for x in graph[temp]:
            # 현재 시간과 추가 시간 갱신
            result[x] = max(result[x], result[temp] + result[x])
            indegree[x] -= 1
            # 차수가 0 이라면 큐에 삽입
            if indegree[x] == 0:
                q.append(x)

    # 출력
    for i in range(1, n + 1):
        print(result[i])


topology_sort()
