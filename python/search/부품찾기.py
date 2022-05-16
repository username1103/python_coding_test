# 5
# 8 3 7 9 2
# 3
# 5 7 9
import sys

# 이진탐색 구현


def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)


# 총 부품의 수와 부품 입력받기 & 이진탐색을 위해 오름차순 정렬하기
n = int(input())
having_data = sorted(list(map(int, sys.stdin.readline().rstrip().split())))

# 원하는 상품 입력 받기
m = int(input())
request_data = list(map(int, sys.stdin.readline().rstrip().split()))

# 각 상품별로 존재 유뮤에 따라 yes ,no 출력
for i in range(len(request_data)):
    result = binary_search(having_data, request_data[i], 0, n - 1)
    if result == None:
        print("no", end=" ")
    else:
        print("yes", end=" ")


# 계수정렬이나 집합자료형을 이용하여서 풀이도 가능
