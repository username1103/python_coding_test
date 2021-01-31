# 5
# 8 3 7 9 2
# 3
# 5 7 9
import sys


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


n = int(input())
having_data = sorted(list(map(int, sys.stdin.readline().rstrip().split())))

m = int(input())
request_data = list(map(int, sys.stdin.readline().rstrip().split()))

for i in range(len(request_data)):
    result = binary_search(having_data, request_data[i], 0, n - 1)
    if result == None:
        print("no", end=" ")
    else:
        print("yes", end=" ")
