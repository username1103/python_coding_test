# 6 4
# 1 4
# 2 3
# 2 4
# 5 6

def find_parent(parent, x):
    if parent[x][0] != x:
        # path compression
        parent[x][0] = find_parent(parent, parent[x][0])
        return parent[x][0]
    return x


def union(parent, x, y):
    x_root = find_parent(parent, x)
    y_root = find_parent(parent, y)

    # rank를 비교해서 rank가 큰 쪽에 하위 트리로 넣기
    if parent[x_root][1] == parent[y_root][1]:
        parent[x_root][1] += 1
        parent[y_root][0] = x_root
    elif parent[x_root][1] > parent[y_root][1]:
        parent[y_root][0] = x_root
    else:
        parent[x_root][0] = y_root

    print(parent)


v, e = map(int, input().split())
parent = [[0] * 2 for _ in range(v + 1)]


for i in range(1,  v + 1):
    parent[i][0] = i
    # rank
    parent[i][1] = 1


for i in range(e):
    x, y = map(int, input().split())
    union(parent, x, y)

print("각 원소가 속한 집합 : ", end='')
for i in range(1, v + 1):
    print(find_parent(parent, i), end=" ")

print()

print("부모 테이블 : ", end="")
for i in range(1, v + 1):
    print(parent[i][0], end=" ")
