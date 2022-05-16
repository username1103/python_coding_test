# 6 4
# 1 4
# 2 3
# 2 4
# 5 6

def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x


def union(parent, x, y):
    x_root = find_parent(parent, x)
    y_root = find_parent(parent, y)

    if x_root < y_root:
        parent[y_root] = x_root
    else:
        parent[x_root] = y_root


v, e = map(int, input().split())
parent = [0] * (v + 1)
for i in range(1,  v + 1):
    parent[i] = i

for i in range(e):
    x, y = map(int, input().split())
    union(parent, x, y)

print("각 원소가 속한 집합 : ", end='')
for i in range(1, v + 1):
    print(find_parent(parent, i), end=" ")

print()

print("부모 테이블 : ", end="")
for i in range(1, v + 1):
    print(parent[i], end=" ")
