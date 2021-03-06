# BaekJoon 18352
# 어떤 나라에는 1번부터 N번까지의 도시와 M개의 단방향 도로가 존재한다. 모든 도로의 거리는 1이다.

# 이 때 특정한 도시 X로부터 출발하여 도달할 수 있는 모든 도시 중에서,
# 최단 거리가 정확히 K인 모든 도시들의 번호를 출력하는 프로그램을 작성하시오.
# 또한 출발 도시 X에서 출발 도시 X로 가는 최단 거리는 항상 0이라고 가정한다.

# 예를 들어 N=4, K=2, X=1일 때 다음과 같이 그래프가 구성되어 있다고 가정하자.


# 이 때 1번 도시에서 출발하여 도달할 수 있는 도시 중에서, 최단 거리가 2인 도시는 4번 도시 뿐이다.
# 2번과 3번 도시의 경우, 최단 거리가 1이기 때문에 출력하지 않는다.

# 입력
# 첫째 줄에 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X가 주어진다.
# (2 ≤ N ≤ 300,000, 1 ≤ M ≤ 1,000,000, 1 ≤ K ≤ 300,000, 1 ≤ X ≤ N)
# 둘째 줄부터 M개의 줄에 걸쳐서 두 개의 자연수 A, B가 공백을 기준으로 구분되어 주어진다.
# 이는 A번 도시에서 B번 도시로 이동하는 단방향 도로가 존재한다는 의미다. (1 ≤ A, B ≤ N)
# 단, A와 B는 서로 다른 자연수이다.

# 출력
# X로부터 출발하여 도달할 수 있는 도시 중에서, 최단 거리가 K인 모든 도시의 번호를 한 줄에 하나씩 오름차순으로 출력한다.

# 이 때 도달할 수 있는 도시 중에서, 최단 거리가 K인 도시가 하나도 존재하지 않으면 -1을 출력한다.

# 예시
# 4 4 2 1
# 1 2
# 1 3
# 2 3
# 2 4

# 4

# 4 3 2 1
# 1 2
# 1 3
# 1 4

# -1

# 4 4 1 1
# 1 2
# 1 3
# 2 3
# 2 4

# 2
# 3
from collections import deque
import sys

# 입력받기
n, m, k, x = map(int, sys.stdin.readline().rstrip().split())

graph = [[] for _ in range(n + 1)]

# 입력 받는 데이터 수가 많으므로 시간초과를 우려해서 sys.stdin.readline이용
# 인접 리스트 방식으로 저장
for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)


def bfs(x):
    # 거리 정보를 저장하고 해당 노드를 지나갔는지 체크하기 위한 리스트
    result = [-1] * (n + 1)
    q = deque()
    # 시작 점을 큐에 넣고 거리 정보 갱신
    q.append(x)
    result[x] = 0
    while q:
        now = q.popleft()

        # 해당 노드와 연결된 모든 노드들에 대한 검사
        for connect in graph[now]:
            # 만약 해당 노드를 방문하지 않았다면
            if result[connect] == -1:
                # 거리를 갱신해주고 큐에 삽입
                result[connect] = result[now] + 1
                q.append(connect)

    return result


# 시작 점에서 부터 bfs 수행
result = bfs(x)
check = False
for i in range(1, len(result)):
    # 거리가 k인 좌표가 있다면 출력
    if result[i] == k:
        print(i)
        check = True

if not check:
    print(-1)
