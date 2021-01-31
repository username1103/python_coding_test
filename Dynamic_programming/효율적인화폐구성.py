# 2 15
# 2
# 3

# 3 4
# 3
# 5
# 7

n, m = map(int, input().split())
data = []
for i in range(n):
    data.append(int(input()))

d = [10001] * (m + 1)
d[0] = 0

# 내 풀이

for i in range(1, m + 1):
    temp = [i - j for j in data if i - j >= 0]
    if not temp:
        continue
    d[i] = min(d[k] for k in temp) + 1

# 답지 풀이

# for i in range(n):
#     for j in range(data[i], m + 1):
#         if d[j - data[i]] != 10001:  # 없어도 되는 부분 b/c 어차피 d[j -data[i]] 가 10001이 더라도 항상 d[j]값을 반환하기 때문에
#             d[j] = min(d[j - data[i]] + 1, d[j])

if d[m] >= 10001:
    print(-1)
else:
    print(d[m])
