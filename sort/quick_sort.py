array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
array_py = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array, start, end):
    # 리스트의 원소가 하나면 종료
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end
    while left <= right:
        # pivot보다 큰 데이터를 찾을 때 까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # pivot보다 작은 데이터를 찾을 때 까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1

        if left > right:  # 엇갈렸다면?
            array[right], array[pivot] = array[pivot], array[right]
        else:  # 엇갈리지 않았다면?
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


quick_sort(array, 0, len(array) - 1)
print(array)


# 시간면에서 조금 더 비효율적
def quick_sort_py(array):
    if len(array) <= 1:
        return array

    pivot = array[0]  # pivot
    tail = array[1:]  # pivot을 제외안 리스트

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort_py(left_side) + [pivot] + quick_sort_py(right_side)


print(quick_sort_py(array_py))
