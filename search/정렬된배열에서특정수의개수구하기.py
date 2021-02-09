# 7 2
# 1 1 2 2 2 2 3

# 7 4
# 1 1 2 2 2 2 3

import bisect
import sys
input = sys.stdin.readline

n, x = map(int, input().split())

num = list(map(int, input().split()))

start = bisect.bisect_left(num, x)
end = bisect.bisect_right(num, x)

if start == end:
    print(-1)
else:
    print(end - start)
