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

# union find 알고리즘
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


# 탑승구의 수
g = int(input())
# 비행기의 수
p = int(input())

# 부모 테이블
parent = [i for i in range(g + 1)]

result = 0
# p개의 비행기들이 순서대로 들어옴
for _ in range(p):
    # 부모를 확인
    data = find_parent(parent, int(input()))
    # 부모가 0인 경우 꽉찼음을 의미
    if data == 0:
        break
    # 부모가 0이 아니면 즉, 꽉차지 않았다면 비행기를 추가
    union(parent, data, data - 1)
    result += 1

print(result)
