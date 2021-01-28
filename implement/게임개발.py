# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1

def rotate(cd):
    return (cd + 3) % 4


nesw_go = [[0, -1], [1, 0], [0, 1], [-1, 0]]
nesw_back = [[0, 1], [-1, 0], [1, 0], [0, -1]]
n, m = list(map(int, input().split()))
cx, cy, cd = list(map(int, input().split()))

_map = []


for _ in range(n):
    _map.append(list(map(int, input().split())))

cnt = 1
rotateCnt = 0

_map[cy][cx] = 2
while True:
    print(cx, cy, cd)
    cd = rotate(cd)
    rotateCnt += 1
    nx = cx + nesw_go[cd][0]
    ny = cy + nesw_go[cd][1]

    if nx < 0 or ny < 0 or nx >= m or ny >= n:
        continue
    elif _map[ny][nx] == 0:
        _map[ny][nx] = 2
        rotateCnt = 0
        cx, cy = nx, ny
        cnt += 1
    elif rotateCnt == 4:
        nx = cx + nesw_back[cd][0]
        ny = cy + nesw_back[cd][1]
        if _map[ny][nx] == 1:
            break
        else:
            cx, cy = nx, ny
    elif _map[ny][nx] == 1 or _map[ny][nx] == 2:
        continue


print(cnt)
