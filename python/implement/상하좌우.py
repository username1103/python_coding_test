# 5
# R R R U D D


lrud = {'L': [0, -1], 'R': [0, 1], 'U': [-1, 0], 'D': [1, 0]}

n = int(input())
x, y = 1, 1
data = input().split()

for direction in data:
    nx = x + lrud[direction][0]
    ny = y + lrud[direction][1]

    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    x, y = nx, ny

print(x, y)
