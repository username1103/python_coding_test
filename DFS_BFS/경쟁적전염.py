# BaekJoon 18405
# NxN 크기의 시험관이 있다. 시험관은 1x1 크기의 칸으로 나누어지며,
# 특정한 위치에는 바이러스가 존재할 수 있다. 모든 바이러스는 1번부터 K번까지의 바이러스 종류 중 하나에 속한다.

# 시험관에 존재하는 모든 바이러스는 1초마다 상, 하, 좌, 우의 방향으로 증식해 나간다.
# 단, 매 초마다 번호가 낮은 종류의 바이러스부터 먼저 증식한다.
# 또한 증식 과정에서 특정한 칸에 이미 어떠한 바이러스가 존재한다면, 그 곳에는 다른 바이러스가 들어갈 수 없다.

# 시험관의 크기와 바이러스의 위치 정보가 주어졌을 때, S초가 지난 후에 (X,Y)에 존재하는 바이러스의 종류를 출력하는 프로그램을 작성하시오.
# 만약 S초가 지난 후에 해당 위치에 바이러스가 존재하지 않는다면, 0을 출력한다.
# 이 때 X와 Y는 각각 행과 열의 위치를 의미하며, 시험관의 가장 왼쪽 위에 해당하는 곳은 (1,1)에 해당한다.

# 예를 들어 다음과 같이 3x3 크기의 시험관이 있다고 하자.
# 서로 다른 1번, 2번, 3번 바이러스가 각각 (1,1), (1,3), (3,1)에 위치해 있다. 이 때 2초가 지난 뒤에 (3,2)에 존재하는 바이러스의 종류를 계산해보자.
# 1 0 2
# 0 0 0
# 3 0 0

# 1초가 지난 후에 시험관의 상태는 다음과 같다.
# 1 1 2
# 1 0 2
# 3 3 0

# 2초가 지난 후에 시험관의 상태는 다음과 같다.
# 1 1 2
# 1 1 2
# 3 3 2

# 결과적으로 2초가 지난 뒤에 (3,2)에 존재하는 바이러스의 종류는 3번 바이러스다. 따라서 3을 출력하면 정답이다.

# 입력
# 첫째 줄에 자연수 N, K가 공백을 기준으로 구분되어 주어진다. (1 ≤ N ≤ 200, 1 ≤ K ≤ 1,000) 둘째 줄부터 N개의 줄에 걸쳐서 시험관의 정보가 주어진다.
# 각 행은 N개의 원소로 구성되며, 해당 위치에 존재하는 바이러스의 번호가 공백을 기준으로 구분되어 주어진다.
# 단, 해당 위치에 바이러스가 존재하지 않는 경우 0이 주어진다. 또한 모든 바이러스의 번호는 K이하의 자연수로만 주어진다.
# N+2번째 줄에는 S, X, Y가 공백을 기준으로 구분되어 주어진다. (0 ≤ S ≤ 10,000, 1 ≤ X, Y ≤ N)

# 출력
# S초 뒤에 (X,Y)에 존재하는 바이러스의 종류를 출력한다. 만약 S초 뒤에 해당 위치에 바이러스가 존재하지 않는다면, 0을 출력한다.

from collections import deque

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

# 시험관 크기와 바이러스 종류 수 입력받기
n, k = map(int, input().split())

m = []

q = []
# 시험관 맵을 입력받고 바이러스의 위치를 큐에 담아줌
for i in range(n):
    m.append(list(map(int, input().split())))
    for j in range(n):
        if m[i][j] != 0:
            q.append((m[i][j], i, j, 0))  # 바이러스의 값, y, x, time 을 저장

# 바이러스 값에 따라 오름차순 정렬
q.sort()

# 타겟시간 타겟좌표 입력받기
ts, ty, tx = map(int, input().split())


def bfs(q):
    q = deque(q)
    while q:
        val, y, x, time = q.popleft()

        # 시간이 타겟시간이 되면 종료
        if time == ts:
            break

        # 4가지 방향으로 탐색진행
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            # 시험관을 벗어나지 않고, 빈공간이라면 바이러스로 채우고 큐에 입력
            if ny >= 0 and nx >= 0 and ny < n and nx < n:
                if m[ny][nx] == 0:
                    m[ny][nx] = val
                    q.append((val, ny, nx, time + 1))


bfs(q)
# 타겟 좌표 출력
print(m[ty - 1][tx - 1])


# heapq 를 이용해서 heappush한 경우 heappop을 이용해서 꺼내야만 순서가 맞춰짐.
# 다르게 꺼낼 경우, 원하는 결과가 나오지 않기도 함.
