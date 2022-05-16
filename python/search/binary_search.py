# 10 7
# 1 3 5 7 9 11 13 15 17 19

# 재귀함수를 이용한 이진 탐색
def binary_search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] < target:
        return binary_search(array, target, mid + 1, end)
    else:
        return binary_search(array, target, start, mid - 1)


# while문을 이용한 이진탐색
def binary_search_while(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return mid


n, target = map(int, input().split())
array = list(map(int, input().split()))

# print(binary_search(array, target, 0, n - 1))
print(binary_search_while(array, target, 0, n - 1))
