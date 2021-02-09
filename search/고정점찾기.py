# 5
# -15 -6 1 3 7

# 7
# -15 -4 2 8 9 13 15

# 7
# -15 -4 3 8 9 13 15


n = int(input())

num = list(map(int, input().split()))

start = 0
end = n
result = -1

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
