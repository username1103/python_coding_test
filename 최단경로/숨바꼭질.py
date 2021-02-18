# 6 7
# 3 6
# 4 3
# 3 2
# 1 3
# 1 2
# 2 4
# 5 2


import heapq

n, m = map(int, input().split())  # 헛간의 수와 연결 수 얻기
INF = 20001  # 최댓값 설정
graph = [[] for _ in range(n)]  # 인접 리스트 이용
# 양방향으로 이동 가능하므로 아래와 같이 그래프 초기화 비용은 모두다 1이므로 따로 비용데이터 추가 X
for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

# 비용 갱신을 위한 테이블
d = [INF] * n

# 시작점 추가
q = []
heapq.heappush(q, (0, 0))  # (비용, 위치) 비용순으로 비교하기 위함

# 다익스트라 알고리즘 수행
while q:
    cost, now = heapq.heappop(q)

    if cost > d[now]:
        continue

    d[now] = cost

    for node in graph[now]:
        ncost = cost + 1  # 비용은 모두다 1이므로
        if ncost < d[node]:
            heapq.heappush(q, (ncost, node))

max_value = 0
max_index = 0
count = 0

for i in range(n):
    # 최댓값을 찾게 되면 해당 인덱스와 값 저장
    if max_value < d[i]:
        max_index = i + 1
        max_value = d[i]
        count = 1
    # 최댓값과 같다면 갯수 추가
    elif max_value == d[i]:
        count += 1

# 출력
print(max_index, max_value, count)
