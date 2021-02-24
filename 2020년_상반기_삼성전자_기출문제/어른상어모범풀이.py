n, m, k = map(int, input().split())

g = []
for i in range(n):
    g.append(list(map(int, input().split())))

directions = list(map(int, input().split()))

# [상어번호, 냄새의 남은시간] 으로 냄새정보를 저장
smell = [[[0, 0]] * n for _ in range(n)]

shark_moveing_rule = [[] for _ in range(m)]
for i in range(m):
    for j in range(4):
        shark_moveing_rule[i].append(list(map(int, input().split())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


# 모든 냄새 정보를 갱신
def update_smell():
    for i in range(n):
        for j in range(n):
            # 냄새 정보가 들어 있다면 1감소
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1
            # 현재 상어가 위치해 있는 곳에 냄새 발생
            if g[i][j] != 0:
                smell[i][j] = [g[i][j], k]


# 모든 상어들이 움직였을 경우를 리턴
def move():
    # 다음 테이블을 담을 임시 테이블
    next_pos = [[0] * n for _ in range(n)]
    for y in range(n):
        for x in range(n):
            # 상어가 존재하는 부분에서
            if g[y][x] != 0:
                direction = directions[g[y][x] - 1]
                found = False  # 갈 수 있는 빈칸이 있는지 여부 False: 없음, True: 있음

                # 상어의 움직임 규칙에 따라 다음 위치들을 확인
                for index in range(4):
                    ny = y + dy[shark_moveing_rule[g[y][x] - 1]
                                [direction - 1][index] - 1]
                    nx = x + dx[shark_moveing_rule[g[y][x] - 1]
                                [direction - 1][index] - 1]

                    # 다음위치가 격자 내에 있고
                    if 0 <= ny < n and 0 <= nx < n:
                        # 다음 위치에 냄새가 존재하지 않는다면
                        if smell[ny][nx][1] == 0:
                            # 상어의 방향 변경
                            directions[g[y][x] - 1] = shark_moveing_rule[g[y]
                                                                         [x] - 1][direction - 1][index]

                            # 다음위치에 상어가 존재하지 않는다면
                            if next_pos[ny][nx] == 0:
                                next_pos[ny][nx] = g[y][x]
                            # 상어가 존재한다면
                            else:
                                next_pos[ny][nx] = min(
                                    next_pos[ny][nx], g[y][x])

                            found = True  # 갈 수 있는길이 존재함을 의미
                            break
                # 갈 수 있는 길이 있다면 다음 상어로 이동
                if found:
                    continue

                # 갈 수 있는 길을 못찾았으므로 자신의 냄새가 있는 곳을 추적
                for index in range(4):
                    ny = y + dy[shark_moveing_rule[g[y][x] - 1]
                                [direction - 1][index] - 1]
                    nx = x + dx[shark_moveing_rule[g[y][x] - 1]
                                [direction - 1][index] - 1]

                    # 격자 내에 있고
                    if 0 <= ny < n and 0 <= nx < n:
                        # 자신의 냄새가 있다면
                        if smell[ny][nx][0] == g[y][x]:
                            # 상어의 방향을 바꾸고
                            directions[g[y][x] - 1] = shark_moveing_rule[g[y]
                                                                         [x] - 1][direction - 1][index]
                            # 상어를 이동
                            next_pos[ny][nx] = g[y][x]
                            break
    return next_pos


# 움직인 시간 정보
time = 0
while True:
    update_smell()  # 현재 위치에 따른 냄새정보 업데이트
    next_pos = move()  # 모든 상어들의 다음위치 정보 얻기
    g = next_pos  # 상어들을 다음위치로 이동시키기
    time += 1

    check = True  # 1번 상어만 남았는지 여부 확인
    for i in range(n):
        for j in range(n):
            if g[i][j] > 1:
                check = False

    # 1번 상어만 남았다면
    if check:
        print(time)
        break

    # 1000초가 되었지만 1번 상어만 존재하는 것이 아니라면
    if time >= 1000:
        print(-1)
        break
