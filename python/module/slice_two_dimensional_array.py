# start, start + count 로 이해하면 쉬움

def slice_two_dimensional_array(arr,rowStart,rowEnd,colStart,colEnd):
    return [row[colStart:colEnd] for row in arr[rowStart:rowEnd]]


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    print("Before Matrix")
    for i in range(len(matrix)):
        print(matrix[i])
    matrix = slice_two_dimensional_array(matrix, 0,2,0,2)
    print()
    print("After Matrix")
    for i in range(len(matrix)):
        print(matrix[i])