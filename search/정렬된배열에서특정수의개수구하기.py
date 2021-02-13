# 7 2
# 1 1 2 2 2 2 3

# 7 4
# 1 1 2 2 2 2 3

import bisect
import sys


def first(num, x, start, end):  # bisect_left
    while start <= end:
        mid = (start + end) // 2
        # num[mid] 값이 target과 같고 왼쪽 값이 없거나 또는 작다면 우리가 찾는 target의 첫번째 인덱스에 도달한 것
        if (mid == 0 or x > num[mid - 1]) and num[mid] == x:
            return mid
        # num[mid]가 target보다 크거나, target과 같지만 왼쪽값이 있고 그 값이 num[mid]와 같다면 첫 좌표를 찾기 위해 end를 땡겨옴
        elif num[mid] >= x:
            end = mid - 1
        # num[mid]가 target보다 작으면 start를 땡겨와 탐색
        else:
            start = mid + 1

    # 해당 값이 존재함을 찾지 못한 경우 None을 리턴
    return None


def last(num, x, start, end):  # bisect_rigth
    while start <= end:
        mid = (start + end) // 2
        # num[mid] 값이 target과 같고, 오른쪽 값이 없거나 있다면 num[mid] 보다 큰경우 마지막인덱스에 도달한 것을 의미
        if (mid == n - 1 or x < num[mid + 1]) and num[mid] == x:
            return mid
        # num[mid] 가 target보다 크다면 end를 땡겨와서 탐색
        elif num[mid] > x:
            end = mid - 1
        # num[mid]가 target보다 작거나, target과 같지만 오른쪽 값이 존재하고 그 값이 num[mid]와 같다면 마지막 좌표를 찾기위해 start를 땡겨옴
        else:
            start = mid + 1

    # 해당 값이 존재하지 않을 경우 도달가능한 부분으로 None 리턴
    return None


def count_by_value(num, x):
    n = len(num)
    # 첫 인덱스 찾기
    a = first(num, x, 0, n - 1)

    # 첫 인덱스가 없다면, 즉, 해당 값이 없다면 return 0
    if a == None:
        return 0

    # 끝 인덱스 찾기
    b = last(num, x, 0, n - 1)

    return b - a + 1


input = sys.stdin.readline

# 총 숫자의 개수와 개수를 알기 원하는 숫자 입력받기
n, x = map(int, input().split())

# 오름차순 졍렬된 숫자데이터 입력받기
num = list(map(int, input().split()))


# bisect 라이브러리 사용
# 이진 탐색을 이용해 해당 숫자의 처음과 끝을 탐색
# start = bisect.bisect_left(num, x)
# end = bisect.bisect_right(num, x)

# # 처음과 끝이 같다면 해당 숫자가 존재하지 않는 것
# if start == end:
#     print(-1)
# else:
#     print(end - start)


# 함수를 만들어 사용
count = count_by_value(num, x)
if count == 0:
    print(-1)
else:
    print(count)
