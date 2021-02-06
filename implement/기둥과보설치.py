# 2020 카카오 신입 공채
# 빙하가 깨지면서 스노우타운에 떠내려 온 죠르디는 인생 2막을 위해 주택 건축사업에 뛰어들기로 결심하였습니다.
# 죠르디는 기둥과 보를 이용하여 벽면 구조물을 자동으로 세우는 로봇을 개발할 계획인데,
# 그에 앞서 로봇의 동작을 시뮬레이션 할 수 있는 프로그램을 만들고 있습니다.
# 프로그램은 2차원 가상 벽면에 기둥과 보를 이용한 구조물을 설치할 수 있는데,
# 기둥과 보는 길이가 1인 선분으로 표현되며 다음과 같은 규칙을 가지고 있습니다.

# 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.
# 보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.
# 단, 바닥은 벽면의 맨 아래 지면을 말합니다.

# 2차원 벽면은 n x n 크기 정사각 격자 형태이며, 각 격자는 1 x 1 크기입니다.
# 맨 처음 벽면은 비어있는 상태입니다. 기둥과 보는 격자선의 교차점에 걸치지 않고, 격자 칸의 각 변에 정확히 일치하도록 설치할 수 있습니다.
# 다음은 기둥과 보를 설치해 구조물을 만든 예시입니다.

# 기둥과보-1.jpg

# 예를 들어, 위 그림은 다음 순서에 따라 구조물을 만들었습니다.

# (1, 0)에서 위쪽으로 기둥을 하나 설치 후, (1, 1)에서 오른쪽으로 보를 하나 만듭니다.
# (2, 1)에서 위쪽으로 기둥을 하나 설치 후, (2, 2)에서 오른쪽으로 보를 하나 만듭니다.
# (5, 0)에서 위쪽으로 기둥을 하나 설치 후, (5, 1)에서 위쪽으로 기둥을 하나 더 설치합니다.
# (4, 2)에서 오른쪽으로 보를 설치 후, (3, 2)에서 오른쪽으로 보를 설치합니다.
# 만약 (4, 2)에서 오른쪽으로 보를 먼저 설치하지 않고,
# (3, 2)에서 오른쪽으로 보를 설치하려 한다면 2번 규칙에 맞지 않으므로 설치가 되지 않습니다.
# 기둥과 보를 삭제하는 기능도 있는데 기둥과 보를 삭제한 후에 남은 기둥과 보들 또한 위 규칙을 만족해야 합니다.
# 만약, 작업을 수행한 결과가 조건을 만족하지 않는다면 해당 작업은 무시됩니다.

# 벽면의 크기 n, 기둥과 보를 설치하거나 삭제하는 작업이 순서대로 담긴 2차원 배열 build_frame이 매개변수로 주어질 때,
# 모든 명령어를 수행한 후 구조물의 상태를 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# n은 5 이상 100 이하인 자연수입니다.
# build_frame의 세로(행) 길이는 1 이상 1,000 이하입니다.
# build_frame의 가로(열) 길이는 4입니다.
# build_frame의 원소는 [x, y, a, b]형태입니다.
# x, y는 기둥, 보를 설치 또는 삭제할 교차점의 좌표이며, [가로 좌표, 세로 좌표] 형태입니다.
# a는 설치 또는 삭제할 구조물의 종류를 나타내며, 0은 기둥, 1은 보를 나타냅니다.
# b는 구조물을 설치할 지, 혹은 삭제할 지를 나타내며 0은 삭제, 1은 설치를 나타냅니다.
# 벽면을 벗어나게 기둥, 보를 설치하는 경우는 없습니다.
# 바닥에 보를 설치 하는 경우는 없습니다.
# 구조물은 교차점 좌표를 기준으로 보는 오른쪽, 기둥은 위쪽 방향으로 설치 또는 삭제합니다.
# 구조물이 겹치도록 설치하는 경우와, 없는 구조물을 삭제하는 경우는 입력으로 주어지지 않습니다.
# 최종 구조물의 상태는 아래 규칙에 맞춰 return 해주세요.
# return 하는 배열은 가로(열) 길이가 3인 2차원 배열로, 각 구조물의 좌표를 담고있어야 합니다.
# return 하는 배열의 원소는 [x, y, a] 형식입니다.
# x, y는 기둥, 보의 교차점 좌표이며, [가로 좌표, 세로 좌표] 형태입니다.
# 기둥, 보는 교차점 좌표를 기준으로 오른쪽, 또는 위쪽 방향으로 설치되어 있음을 나타냅니다.
# a는 구조물의 종류를 나타내며, 0은 기둥, 1은 보를 나타냅니다.
# return 하는 배열은 x좌표 기준으로 오름차순 정렬하며, x좌표가 같을 경우 y좌표 기준으로 오름차순 정렬해주세요.
# x, y좌표가 모두 같은 경우 기둥이 보보다 앞에 오면 됩니다.

# 입출력 예
# 5
# [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
# [[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]

# 5
# [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
# [[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]

import copy

n = 5
build_frame = [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [
    1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]


# 기둥의 가능 여부 체크
def checkPillar(answer, x, y, ex=[]):
    # answer값을 변환 시키지 않기 위해 카피후 만약 제거할 대상이 있다면 대상을 제거 하여 체크
    temp = copy.deepcopy(answer)
    if ex in temp:
        temp.remove(ex)
    val1 = isOnPillar(temp, x, y)
    val2 = isOnstep(temp, x, y)
    return val1 or val2


# 기둥위에 있는지 체크
def isOnPillar(answer, x, y):
    if len(answer) == 0:
        return False
    for data in answer:
        if data[2] == 0 and data[0] == x and data[1] == y-1:
            return True
    return False


# 보 위에 있는 지 체크
def isOnstep(answer, x, y):
    if len(answer) == 0:
        return False

    for data in answer:
        if data[2] == 1 and data[1] == y and (data[0] == x or data[0] == x-1):
            return True

    return False


# 해당 아이템의 answer에서 index를 찾음
def findItem(answer, x, y, item_type):
    for i in range(len(answer)):
        if answer[i][2] == item_type and answer[i][0] == x and answer[i][1] == y:
            return i


# 보에 대한 체크
def checkStep(answer, x, y, ex=[]):
    if len(answer) == 0:
        return False
    # answer의 값을 바꾸지 않기 위해 copy하여 제거하는 경우 해당 항목을 제거
    temp = copy.deepcopy(answer)
    if ex in temp:
        temp.remove(ex)

    for data in temp:
        # 기둥이 아래에 있거나
        if data[2] == 0:
            if data[1] == y - 1 and (data[0] == x or data[0] == x + 1):
                return True
        # 양쪽에 보가 있다면
        else:
            if inlineStep(temp, x, y):
                return True

    return False


def inlineStep(answer, x, y):
    if [x-1, y, 1] in answer and [x+1, y, 1] in answer:
        return True
    return False


# 현재 기둥에 대한 연결된 보나 기둥을 리턴
def get_connectPillar(answer, x, y):
    out = []
    if [x, y+1, 0] in answer:
        out.append([x, y+1, 0])
    if [x-1, y+1, 1] in answer:
        out.append([x-1, y+1, 1])
    if [x, y+1, 1] in answer:
        out.append([x, y+1, 1])

    return out


# 현재 보에 연결된 보나 기둥을 리턴
def get_connectStep(answer, x, y):
    out = []
    if [x, y, 0] in answer:
        out.append([x, y, 0])
    if [x+1, y, 0] in answer:
        out.append([x+1, y, 0])
    if [x-1, y, 1] in answer:
        out.append([x-1, y, 1])
    if [x+1, y, 1] in answer:
        out.append([x+1, y, 1])

    return out


def solution(n, build_frame):
    answer = []

    # 각 프레임에 대하여
    for frame in build_frame:
        x, y, item_type, do_type = frame
        # 기둥이라면
        if item_type == 0:
            # 설치라면
            if do_type == 1:
                # 유효한 설치인지 체크
                if y == 0 or isOnPillar(answer, x, y) or isOnstep(answer, x, y):
                    answer.append([x, y, 0])
            # 삭제라면
            else:
                play = True
                # 연결된 기둥이나 보 데이터를 얻어옴
                connect_list = get_connectPillar(answer, x, y)
                # 해당 데이터들이 현재 기둥이 없어졌을 때 타당한지 체크
                for item in connect_list:
                    if item[2] == 0:
                        if item[1] != 0 and not checkPillar(answer, item[0], item[1], [x, y, item_type]):
                            play = False
                            break
                    if item[2] == 1:
                        if not checkStep(answer, item[0], item[1], [x, y, item_type]):
                            play = False
                            break
                # 타당하다면 해당 기둥을 제거
                if play == True:
                    index = findItem(answer, x, y, item_type)
                    answer.remove(answer[index])
        # 기둥이라면
        else:
            # 설치라면
            if do_type == 1:
                # 타당성 체크 후 설치
                if y != 0 and checkStep(answer, x, y):
                    answer.append([x, y, 1])
            # 삭제라면
            else:
                play = True
                # 보와 연결된 기둥과 보 데이터를 얻어옴
                connect_list = get_connectStep(answer, x, y)

                # 현재 보가 사라질 경우 연결된 보나 기둥에 대한 타당성 체크
                for item in connect_list:
                    if item[2] == 0:
                        if item[1] != 0 and not checkPillar(answer, item[0], item[1], [x, y, item_type]):
                            play = False
                            break
                    if item[2] == 1:
                        if not checkStep(answer, item[0], item[1], [x, y, item_type]):
                            play = False
                            break
                # 삭제해도 괜찮다면 삭제
                if play == True:
                    index = findItem(answer, x, y, item_type)
                    answer.remove(answer[index])

    # x,y,기둥인지 보인지 순으로 비교하여 정렬후 리턴
    return sorted(answer, key=lambda x: [x[0], x[1], x[2]])


print(solution(n, build_frame))
