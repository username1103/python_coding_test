array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i
    # i번 이상에서 가장 작은 데이터 찾기
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    # 가장 작은 데이터를 찾아서 i번째 인덱스와 교환
    array[i], array[min_index] = array[min_index], array[i]

print(array)
