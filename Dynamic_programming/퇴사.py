n = int(input())

data = []
for i in range(n):
    t, p = map(int, input().split())
    data.append((t, p, i + t))  # i + t 가 n보다 크면 기간초과

d = [0] * n

for i in range(len(data)):
    temp = [d[i - 1]]
    for j in range(i + 1):
        if data[j][2] == i + 1:
            temp.append(d[i - data[j][0]] + data[j][1])

    d[i] = max(temp)

print(d[n - 1])
