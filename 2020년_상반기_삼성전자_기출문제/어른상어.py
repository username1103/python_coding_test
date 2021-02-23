from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

n, m, k = map(int, input().split())  # 격자 크기, 상어의 수, 냄새 유지시간 입력받기

live_shark = [True] * m  # 상어들이 살아있는지 체크
graph = []  # 격자 테이블
shark_pos = [deque() for _ in range(m)]  # 상어들의 위치와 냄새를 담을 테이블
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        # 상어가 있다면 상어위치를 추가
        if graph[i][j] != 0:
            shark_pos[graph[i][j] - 1].appendleft((i, j))

# 상어들의 현재 방향 입력받기
direction = list(map(int, input().split()))

# 상어들의 이동 원칙 입력받기
shark_moving_rule = [[] for _ in range(m)]
for i in range(m):
    shark_moving_rule[i].append(list(map(int, input().split())))  # 위
    shark_moving_rule[i].append(list(map(int, input().split())))  # 아래
    shark_moving_rule[i].append(list(map(int, input().split())))  # 왼쪽
    shark_moving_rule[i].append(list(map(int, input().split())))  # 오른쪽


# 상어의 다음 위치 좌표를 리턴함
def move(graph, direction, shark_pos, shark_moving_rule, shark):
    # 상어의 현재위치 와 현재 방향
    now_y, now_x = shark_pos[shark - 1][0][0], shark_pos[shark - 1][0][1]
    now_direction = direction[shark - 1]

    # 현재 방향에 따라 이동원칙을 통한 다음위치 확인
    for i in range(4):
        next_y = now_y + dy[shark_moving_rule[shark - 1]
                            [now_direction - 1][i] - 1]
        next_x = now_x + dx[shark_moving_rule[shark - 1]
                            [now_direction - 1][i] - 1]

        # 격자 내에 있고 해당 자리에 갈 수 있다면
        if 0 <= next_y < n and 0 <= next_x < n:
            if graph[next_y][next_x] == 0:
                direction[shark - 1] = shark_moving_rule[shark -
                                                         1][now_direction - 1][i]
                return (next_y, next_x)

    # 갈 자리가 없어서 해당 위치에서 자신의 냄새가 있는 곳으로 이동
    for i in range(4):
        next_y = now_y + dy[shark_moving_rule[shark - 1]
                            [now_direction - 1][i] - 1]
        next_x = now_x + dx[shark_moving_rule[shark - 1]
                            [now_direction - 1][i] - 1]
        if 0 <= next_y < n and 0 <= next_x < n:
            if graph[next_y][next_x] == shark:
                direction[shark - 1] = shark_moving_rule[shark -
                                                         1][now_direction - 1][i]
                return (next_y, next_x)


# 각 상어들의 다음위치를 담은 리스트 리턴 상어가 죽었다면 None을 담고 있음
def move_all_shark(graph, direction, shark_pos, shark_moving_rule):
    shark_current_pos = [None] * m  # 각 상어들이 다음에 이동할 위치를 담음
    for i in range(m):
        if live_shark[i]:  # 상어가 살아있다면 다음 위치를 얻어옴
            shark_current_pos[i] = move(
                graph, direction, shark_pos, shark_moving_rule, i + 1)

    return shark_current_pos


time = 0  # 총 시간
while True:
    # 모든 상어들을 이동 시킴
    current_pos = move_all_shark(
        graph, direction, shark_pos, shark_moving_rule)
    # 상어의 값이 큰 상어부터 진행
    for i in range(m - 1, -1, -1):
        # 상어의 다음위치가 None이 아니라면, 즉 상어가 살아있다면
        if current_pos[i] != None:
            # 다음위치가 비어있다면 상어를 이동시킴
            if graph[current_pos[i][0]][current_pos[i][1]] == 0:
                graph[current_pos[i][0]][current_pos[i][1]] = i + 1
                shark_pos[i].appendleft((current_pos[i][0], current_pos[i][1]))
            # 다음위치에 다른 상어가 존재할 경우 그 값에 따라 처리
            else:
                # 다음위치에 존재하는 상어가 작은 경우
                if graph[current_pos[i][0]][current_pos[i][1]] > i + 1:
                    # 해당 위치에 상어를 제거하고
                    live_shark[graph[current_pos[i][0]]
                               [current_pos[i][1]] - 1] = False
                    # 옮겨지는 상어를 배치
                    graph[current_pos[i][0]][current_pos[i][1]] = i + 1
                    # 상어의 위치 갱신
                    shark_pos[i].appendleft(
                        (current_pos[i][0], current_pos[i][1]))
                # 다음위치가 만약 자기가 다녀간 곳이라면
                elif graph[current_pos[i][0]][current_pos[i][1]] == i + 1:
                    # 위치 갱신
                    shark_pos[i].appendleft(
                        (current_pos[i][0], current_pos[i][1]))
        # 총 개수 맞추기 위함..
        else:
            shark_pos[i].appendleft((-1, -1))

        # 상어의 냄새까지 총 개수가 k보다 크면
        if len(shark_pos[i]) > k:
            # 가장 먼저 들어간 냄새 제거
            last_y, last_x = shark_pos[i].pop()
            # 쓰레기 값이 아니고, 같은 위치가 상어위치&냄새 테이블에 존재하지 않고, 해당 위치에 좌표가 자신인 경우
            if last_y != -1 and (last_y, last_x) not in shark_pos[i] and graph[last_y][last_x] == i + 1:
                graph[last_y][last_x] = 0

    time += 1  # 총시간 추가
    # 1번 상어만 살아있는지 체크
    check = True
    for i in range(1, m):
        if live_shark[i]:
            check = False
            break

    # 1번 상어만 살아있다면 시간을 출력하고
    if check:
        print(time)
        break

    # 1000번의 이동 안에 1번 상어만 존재하도록 하지 못한다면 -1출력
    if time >= 1000:
        print(-1)
        break
