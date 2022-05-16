# 5 3
# 1 2 5 4 3
# 5 5 6 6 5

n, k = map(int, input().split())
data = []

for _ in range(2):
    data.append(list(map(int, input().split())))

data[0].sort()
data[1].sort(reverse=True)

for i in range(k):
    if data[0][i] < data[1][i]:
        data[0][i] = data[1][i]
    else:
        break

print(sum(data[0]))
