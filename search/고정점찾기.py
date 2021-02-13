# 5
# -15 -6 1 3 7

# 7
# -15 -4 2 8 9 13 15

# 7
# -15 -4 3 8 9 13 15


n = int(input())

num = list(map(int, input().split()))

# 이진탐색을 위한 초기화
start = 0
end = n - 1

# 고정점찾기 위한 초기화 없다면 -1로 그대로 유지
result = -1


# 이진탐색 시작
while start <= end:
    select = (start + end) // 2
    if num[select] == select:
        result = select
        break

    elif num[select] > select:
        end = select - 1
    else:
        start = select + 1

print(result)
