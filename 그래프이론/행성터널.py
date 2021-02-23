# BaekJoon 2887
# 때는 2040년, 이민혁은 우주에 자신만의 왕국을 만들었다. 왕국은 N개의 행성으로 이루어져 있다.
# 민혁이는 이 행성을 효율적으로 지배하기 위해서 행성을 연결하는 터널을 만들려고 한다.

# 행성은 3차원 좌표위의 한 점으로 생각하면 된다. 두 행성 A(xA, yA, zA)와 B(xB, yB, zB)를 터널로 연결할 때 드는 비용은 min(|xA-xB|, |yA-yB|, |zA-zB|)이다.

# 민혁이는 터널을 총 N-1개 건설해서 모든 행성이 서로 연결되게 하려고 한다. 이때, 모든 행성을 터널로 연결하는데 필요한 최소 비용을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 행성의 개수 N이 주어진다. (1 ≤ N ≤ 100,000) 다음 N개 줄에는 각 행성의 x, y, z좌표가 주어진다.
# 좌표는 -109보다 크거나 같고, 109보다 작거나 같은 정수이다. 한 위치에 행성이 두 개 이상 있는 경우는 없다.

# 출력
# 첫째 줄에 모든 행성을 터널로 연결하는데 필요한 최소 비용을 출력한다.

# 5
# 11 -15 -15
# 14 -5 -15
# -1 -1 -5
# 10 -4 -1
# 19 -4 19

# 4


import sys
import heapq
input = sys.stdin.readline


# union find 알고리즘
def find_parent(parent, n):
    if parent[n] != n:
        parent[n] = find_parent(parent, parent[n])
    return parent[n]


def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 행성 개수
n = int(input())

x = []
y = []
z = []

# i번째 행성의 x,y,z를 저장
for i in range(n):
    data = list(map(int, input().split()))
    x.append((data[0], i))
    y.append((data[1], i))
    z.append((data[2], i))

# 부모 테이블 초기화
parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i

# 좌표순으로 정렬
x.sort()
y.sort()
z.sort()

q = []
# 각 행성들의 x,y,z 좌표 차이를 기준으로 오름차순으로 큐에 삽입
for i in range(n-1):
    heapq.heappush(q, (x[i+1][0] - x[i][0], x[i][1], x[i+1][1]))
    heapq.heappush(q, (y[i+1][0] - y[i][0], y[i][1], y[i+1][1]))
    heapq.heappush(q, (z[i+1][0] - z[i][0], z[i][1], z[i+1][1]))

cnt = 0  # 연결횟수
total = 0  # 총 비용
# 크루스칼 알고리즘 진행
while q:
    # n - 1 번의 연결이 진행되면 n개가 연결된 것이므로 종료
    if cnt == n - 1:
        break

    cost, x, y = heapq.heappop(q)
    # 연결되지 않았다면 연결해주고 비용과 연결 횟수 추가
    if find_parent(parent, x) != find_parent(parent, y):
        union(parent, x, y)
        cnt += 1
        total += cost

# 총 비용 출력
print(total)
