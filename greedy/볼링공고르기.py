# 5 3
# 1 3 2 3 2

# 8 5
# 1 5 4 3 2 4 5 2

n, m = map(int, input().split())

ball = list(map(int, input().split()))

cnt = 0
for i in range(len(ball)):
    main = ball[i]
    for weight in ball[i + 1:]:
        if weight != main:
            cnt += 1

print(cnt)
