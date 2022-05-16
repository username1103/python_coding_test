# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1

# 5 5
# 1 1 0
# 1 1 1 1 1
# 1 0 0 1 1
# 1 0 0 0 1
# 1 1 0 1 1
# 1 1 1 1 1


# 왼쪽으로 회전시키기
def rotateLeft(d):
    return (d + 3) % 4


# 뒤로 가는 방향 얻기
def back(d):
    return (d + 2) % 4


dx = [-1, 0, 1, 0]  # x 변화량
dy = [0, 1, 0, -1]  # y 변화량

n, m = map(int, input().split())  # 지도 크기
x, y, d = map(int, input().split())  # 시작 좌표, 방향

info = []  # 맵 정보
for i in range(n):
    info.append(list(map(int, input().split())))

# 첫 위치 방문처리
info[x][y] = 2
total = 1

# 회전수 체크
rotate_cnt = 0
while True:
    # 왼쪽으로 회전
    d = rotateLeft(d)

    # 다음 위치
    nx = x + dx[d]
    ny = y + dy[d]

    # 다음 위치로 이동 가능 하면
    if info[nx][ny] == 0:
        rotate_cnt = 0  # 회전수 초기화
        # 방문처리
        total += 1
        info[nx][ny] = 2
        # 이동
        x = nx
        y = ny
    # 다음 위치로 이동 불가한 경우
    else:
        # 회전 횟수 세기
        rotate_cnt += 1

        # 네 방향을 모두 체크한 경우
        if rotate_cnt == 4:
            rotate_cnt = 0
            # 뒤가 바다 라면
            if info[x + dx[back(d)]][y + dy[back(d)]] == 1:
                break
            # 뒤가 바다가 아니라면
            else:
                # 뒤로 한칸가기
                x = x + dx[back(d)]
                y = y + dy[back(d)]

# 출력
print(total)
