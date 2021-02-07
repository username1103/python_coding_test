from collections import deque

board = [[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [
    0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]


def getNextPos(pos, board):
    next_pos_list = []
    pos = list(pos)
    pos1_y, pos1_x, pos2_y, pos2_x = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    for i in range(4):
        next_pos1_y = pos1_y + dy[i]
        next_pos1_x = pos1_x + dx[i]
        next_pos2_y = pos2_y + dy[i]
        next_pos2_x = pos2_x + dx[i]
        if board[next_pos1_y][next_pos1_x] == 0 and board[next_pos2_y][next_pos2_x] == 0:
            next_pos_list.append(
                {(next_pos1_y, next_pos1_x), (next_pos2_y, next_pos2_x)})

    if pos1_y == pos2_y:
        for i in [-1, 1]:
            if board[pos1_y + i][pos1_x] == 0 and board[pos2_y + i][pos2_x] == 0:
                next_pos_list.append({(pos1_y, pos1_x), (pos1_y+i, pos1_x)})
                next_pos_list.append({(pos2_y, pos2_x), (pos2_y+i, pos2_x)})

    elif pos1_x == pos2_x:
        for i in [-1, 1]:
            if board[pos1_y][pos1_x + i] == 0 and board[pos2_y][pos2_x + i] == 0:
                next_pos_list.append({(pos1_y, pos1_x), (pos1_y, pos1_x + i)})
                next_pos_list.append({(pos2_y, pos2_x), (pos2_y, pos2_x + i)})

    return next_pos_list


def solution(board):
    answer = 0
    n = len(board)
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]

    q = deque()
    visited = []
    pos = {(1, 1), (1, 2)}
    q.append((pos, 0))
    visited.append(pos)
    while q:
        pos, cost = q.popleft()
        if (n, n) in pos:
            return cost

        for next_pos in getNextPos(pos, new_board):
            if next_pos not in visited:
                q.append((next_pos, cost + 1))
                visited.append(next_pos)
    return answer


print(solution(board))
