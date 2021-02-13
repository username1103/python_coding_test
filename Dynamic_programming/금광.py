# 2
# 3 4
# 1 3 3 2 2 1 4 1 0 6 4 7
# 4 4
# 1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2


t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    cave = list(map(int, input().split()))
    d = [0] * (m * n)
    for i in range(n):
        d[i * m] = cave[i * m]
    for j in range(1, m):
        for i in range(n):
            temp = []
            temp.append(d[i * m + (j - 1)])
            if i - 1 >= 0:
                temp.append(d[(i - 1)*m + (j - 1)])
            if i + 1 < n:
                temp.append(d[(i + 1) * m + (j - 1)])
            d[i * m + j] = max(temp) + cave[i * m + j]

    result = 0
    for i in range(n):
        result = max(result, d[i * m + (m - 1)])

    print(result)
