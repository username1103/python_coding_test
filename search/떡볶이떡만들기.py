# 4 6
# 19 15 10 17

import sys

n, target = map(int, input().split())
height = list(map(int, sys.stdin.readline().rstrip().split()))

start = 0
end = max(height)

# 이진탐색 시작
result = 0
while start <= end:
    total = 0
    # 중간값찾기
    select = (start + end) // 2
    for dduk in height:
        # 떡 들중에서 중간값보다 큰 녀석들을 잘라서 길이를 더함
        if dduk > select:
            total += dduk - select

    # target과 비교하여 target보다 작다면 끝점을 땡겨옴
    if total < target:
        end = select - 1
    # target 보다 크거나 같다면 result를 현재 값으로 설정하고
    # start를 땡겨옴
    else:
        result = select
        start = select + 1

print(result)
