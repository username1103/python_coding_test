import sys
import heapq
input = sys.stdin.readline


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


n = int(input())

x = []
y = []
z = []
for i in range(n):
    data = list(map(int, input().split()))
    x.append((data[0], i))
    y.append((data[1], i))
    z.append((data[2], i))


parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i

x.sort()
y.sort()
z.sort()

q = []
for i in range(n-1):
    heapq.heappush(q, (x[i+1][0] - x[i][0], x[i][1], x[i+1][1]))
    heapq.heappush(q, (y[i+1][0] - y[i][0], y[i][1], y[i+1][1]))
    heapq.heappush(q, (z[i+1][0] - z[i][0], z[i][1], z[i+1][1]))

cnt = 0
total = 0
while q:
    if cnt == n - 1:
        break
    cost, x, y = heapq.heappop(q)
    if find_parent(parent, x) != find_parent(parent, y):
        union(parent, x, y)
        cnt += 1
        total += cost

print(total)
