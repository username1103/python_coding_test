# 4
# 3
# 4
# 1
# 1

# 2

# 4
# 6
# 2
# 2
# 3
# 3
# 4
# 4

# 3

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y


g = int(input())
p = int(input())

parent = [i for i in range(g + 1)]

result = 0
for _ in range(p):
    data = find_parent(parent, int(input()))
    if data == 0:
        break
    union(parent, data, data - 1)
    result += 1

print(result)
