# 4 6
# 19 15 10 17

import sys

n, target = map(int, input().split())
height = list(map(int, sys.stdin.readline().rstrip().split()))

start = 0
end = max(height)
result = 0

while start <= end:
    total = 0
    select = (start + end) // 2
    for dduk in height:
        if dduk > select:
            total += dduk - select

    if total < target:
        end = select - 1
    else:
        result = select
        start = select + 1

print(result)
