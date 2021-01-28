# chapter3 greedy 3-1
# 5 8 3
# 2 4 5 4 6


n, m, k = list(map(int, input().split()))
data = sorted(list(map(int, input().split())))

result = 0
temp = 0
cnt = 0

while temp < m:
    temp += 1
    if cnt == k:
        result += data[n - 2]
        cnt = 0
    else:
        result += data[n - 1]
        cnt += 1

print(result)

# 3-2
first = data[n - 1]
second = data[n - 2]

# 가장 큰 수가 더해지는 횟수
count = int(m / (k + 1)) * k + (m % (k + 1))

result = 0
result += count * first
result += (m - count) * second

print(result)
