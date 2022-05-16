def rotate90(matrix):
    cntRow = len(matrix)
    cntCol = len(matrix[0])
    # 변환될 메트릭스 크기 생성
    result = [[0] * cntRow for _ in range(cntCol)]

    # 변환전 데이터의 col값은 변환후 데이터의 row값과 같음
    # 변환전 데이터의 row값은 변환 후 데이터의 끝에서 row값만 큼 뺀 col값에 위치
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
