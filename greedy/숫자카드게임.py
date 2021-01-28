# 3 3
# 3 1 2
# 4 1 4
# 2 2 2

# 2 4
# 7 3 1 8
# 3 3 3 4

row, col = list(map(int, input().split()))
data = []
for _ in range(row):
    data.append(min(list(map(int, input().split()))))

print(max(data))
