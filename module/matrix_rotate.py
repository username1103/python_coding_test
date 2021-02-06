def rotate90(matrix):
    cntRow = len(matrix)
    cntCol = len(matrix[0])
    # 초기화
    result = [[0] * cntRow for _ in range(cntCol)]

    for row in range(cntRow):
        for col in range(cntCol):
            result[col][cntRow - 1 - row] = matrix[row][col]
    return result


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    print("Before Matrix")
    for i in range(len(matrix)):
        print(matrix[i])
    matrix = rotate90(matrix)
    print()
    print("After Matrix")
    for i in range(len(matrix)):
        print(matrix[i])
