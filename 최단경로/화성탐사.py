# 3
# 3
# 5 5 4
# 3 9 1
# 3 2 7
# 5
# 3 7 2 0 1
# 2 8 0 9 1
# 1 2 1 8 1
# 9 8 9 2 0
# 3 6 5 1 5
# 7
# 9 0 5 1 1 5 3
# 4 1 2 1 6 5 3
# 0 7 6 1 6 8 5
# 1 1 7 8 3 2 3
# 9 4 0 7 6 4 1
# 5 8 3 2 4 8 3
# 7 4 8 4 8 3 4

import heapq

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
t = int(input())  # 총 진행 횟수

for _ in range(t):
    n = int(input())  # 맵의 크기
    INF = n * n * 9 + 1  # 최댓값 설정
    g = []  # 그래프 인접행렬 이용
    d = [[INF] * n for _ in range(n)]  # 다익스트라 알고리즘을 위한 테이블
    for i in range(n):
        g.append(list(map(int, input().split())))  # 그래프 초기화

    q = []
    heapq.heappush(q, (g[0][0], 0, 0))  # 비용순으로 비교하기 위해 다음과 같이 설정
    while q:
        cost, y, x = heapq.heappop(q)

        # 선택된 곳 까지의 비용이 테이블에 저장된 비용보다 크다면 무시
        if cost > d[y][x]:
            continue

        # 테이블 값 초기화
        d[y][x] = cost

        # 4가지 방향에 대한 확인
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            # 그래프를 벗어나지 않았다면
            if 0 <= ny < n and 0 <= nx < n:
                # 해당 위치까지 비용 체크
                ncost = cost + g[ny][nx]
                # 비용이 테이블에 비용보다 작다면 추가
                if ncost < d[ny][nx]:
                    heapq.heappush(q, (ncost, ny, nx))

    # 출력
    print(d[n-1][n-1])
