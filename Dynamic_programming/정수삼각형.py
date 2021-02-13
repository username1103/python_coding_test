n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

d = [[0] * i for i in range(1, n + 1)]
d[0][0] = data[0][0]

result = 0
for i in range(1, len(data)):
    for j in range(len(data[i])):
        if j == 0:
            d[i][j] = max(d[i][j], d[i-1][j] + data[i][j])
        elif j == len(data[i]) - 1:
            d[i][j] = max(d[i][j], d[i-1][j-1] + data[i][j])
        else:
            d[i][j] = max(d[i][j], d[i-1][j] + data[i]
                          [j], d[i-1][j-1] + data[i][j])

        if i == len(data) - 1:
            result = max(result, d[i][j])

print(result)
