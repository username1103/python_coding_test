# 5 4
# 0 1 0 1 1
# 1 0 1 1 0
# 0 1 0 0 0
# 1 1 0 0 0
# 1 0 0 0 0
# 2 3 4 3


# union find 알고리즘
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


# 여행지 수, 여행계획에 속한 도시 수
n, m = map(int, input().split())

# 부모 확인 테이블
parent = [i for i in range(n)]


# 길이 존재하는 여행지 끼리 합쳐줌
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(i + 1, n):
        if temp[j] == 1:
            union(parent, i, j)

# 여행할 도시 들
plan = list(map(int, input().split()))

cango = True
r = find_parent(parent, plan[0] - 1)  # 첫번째 여행지의 부모를 확인
for i in range(1, m):
    # 부모가 다른 여행지가 존재한다면. 즉, 갈 수 있는 길이 없다는 것
    if r != find_parent(parent, plan[i] - 1):
        cango = False

if cango:
    print("YES")
else:
    print("NO")
