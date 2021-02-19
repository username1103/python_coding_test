# 5 4
# 0 1 0 1 1
# 1 0 1 1 0
# 0 1 0 0 0
# 1 1 0 0 0
# 1 0 0 0 0
# 2 3 4 3

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())

parent = [i for i in range(n)]

graph = [[] for _ in range(n)]
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(i + 1, n):
        if temp[j] == 1:
            union(parent, i, j)

plan = list(map(int, input().split()))

cango = True
r = find_parent(parent, plan[0] - 1)
for i in range(1, m):
    if r != find_parent(parent, plan[i] - 1):
        cango = False

if cango:
    print("YES")
else:
    print("NO")
