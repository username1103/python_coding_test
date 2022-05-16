# a1

# c2

move = [[-2, -1], [-2, 1], [2, 1], [2, -1], [-1, 2], [1, 2], [1, -2], [-1, -2]]

loc = input()

col = ord(loc[0]) - ord('a') + 1
row = int(loc[1])

cnt = 0

for direction in move:
    nx = row + direction[0]
    ny = col + direction[1]

    if nx < 1 or ny < 1 or nx > 8 or ny > 8:
        continue

    cnt += 1


print(cnt)
