# 2020 카카오 신입 공채
# 고고학자인 튜브는 고대 유적지에서 보물과 유적이 가득할 것으로 추정되는 비밀의 문을 발견하였습니다.
# 그런데 문을 열려고 살펴보니 특이한 형태의 자물쇠로 잠겨 있었고
# 문 앞에는 특이한 형태의 열쇠와 함께 자물쇠를 푸는 방법에 대해 다음과 같이 설명해 주는 종이가 발견되었습니다.

# 잠겨있는 자물쇠는 격자 한 칸의 크기가 1 x 1인 N x N 크기의 정사각 격자 형태이고 특이한 모양의 열쇠는 M x M 크기인 정사각 격자 형태로 되어 있습니다.

# 자물쇠에는 홈이 파여 있고 열쇠 또한 홈과 돌기 부분이 있습니다.
# 열쇠는 회전과 이동이 가능하며 열쇠의 돌기 부분을 자물쇠의 홈 부분에 딱 맞게 채우면 자물쇠가 열리게 되는 구조입니다.
# 자물쇠 영역을 벗어난 부분에 있는 열쇠의 홈과 돌기는 자물쇠를 여는 데 영향을 주지 않지만,
# 자물쇠 영역 내에서는 열쇠의 돌기 부분과 자물쇠의 홈 부분이 정확히 일치해야 하며 열쇠의 돌기와 자물쇠의 돌기가 만나서는 안됩니다.
# 또한 자물쇠의 모든 홈을 채워 비어있는 곳이 없어야 자물쇠를 열 수 있습니다.

# 열쇠를 나타내는 2차원 배열 key와 자물쇠를 나타내는 2차원 배열 lock이 매개변수로 주어질 때,
# 열쇠로 자물쇠를 열수 있으면 true를, 열 수 없으면 false를 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# key는 M x M(3 ≤ M ≤ 20, M은 자연수)크기 2차원 배열입니다.
# lock은 N x N(3 ≤ N ≤ 20, N은 자연수)크기 2차원 배열입니다.
# M은 항상 N 이하입니다.
# key와 lock의 원소는 0 또는 1로 이루어져 있습니다.
# 0은 홈 부분, 1은 돌기 부분을 나타냅니다.

# 입출력 예
# [[0, 0, 0], [1, 0, 0], [0, 1, 1]]	[[1, 1, 1], [1, 1, 0], [1, 0, 1]]
# true
import copy

key = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
lock = [[1, 1, 1], [1, 1, 1], [1, 1, 0]]


# 회전전의 열번호는 회전후의 행번호와 일치
# 회전후의 열은 N-1에서 회전전의 행을 뺀 값
def rotate90(key):
    key_length = len(key)
    out = [[0]*key_length for _ in range(key_length)]
    for i in range(key_length):
        for j in range(key_length):
            out[i][j] = key[key_length - 1 - j][i]
    return out


# big_lock 에서 lock에 해당하는 부분이 모두 1이라면 true 아니라면 false
def check(big_lock, key, lock,  i, j):
    for k in range(len(key)):
        for l in range(len(key)):
            big_lock[i + k][j + l] += key[k][l]

    for i in range(len(lock)):
        for j in range(len(lock)):
            if big_lock[len(key) - 1 + i][len(key) - 1 + j] != 1:
                return False

    return True


def solution(key, lock):
    answer = False
    key_length = len(key)
    lock_length = len(lock)
    big_lock = [[0] * (lock_length + (key_length - 1) * 2)
                for _ in range(lock_length + (key_length - 1) * 2)]  # big_lock의 크기는 (key의 크기 - 1) 만큼 상하좌우를 키움
    # big_lock에 lock값을 가운데에 넣어줌
    for i in range(lock_length):
        for j in range(lock_length):
            big_lock[i+key_length-1][j+key_length-1] = lock[i][j]

    # 회전시켜 가며 총 4번 확인
    for r in range(4):
        if r > 0:
            key = rotate90(key)
        for i in range(len(big_lock) - key_length + 1):
            for j in range(len(big_lock) - key_length + 1):
                temp = copy.deepcopy(big_lock)
                answer = check(temp, key, lock, i, j)
                if answer == True:
                    return answer

    return answer


print(solution(key, lock))

# 아이디어
# lock의 크기를 키워 key를 끝에서부터 비교하도록 하는 방법
