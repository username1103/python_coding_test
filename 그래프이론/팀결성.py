# 7 8
# 0 1 3
# 1 1 7
# 0 7 6
# 1 7 1
# 0 3 7
# 0 4 2
# 0 1 1
# 1 1 1
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
        return parent[x]
    return x


def union(x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


# 학생 수와 연산 수 입력받기
n, m = map(int, input().split())

# 부모 테이블 초기화
parent = [i for i in range(n + 1)]

# 주어진 연산에 따라 연산 수행
for i in range(m):
    t, a, b = map(int, input().split())
    if t == 0:
        union(a, b)
    else:
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")
