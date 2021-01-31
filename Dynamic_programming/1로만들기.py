# 26

import sys
x = int(input())
d = [0] * 30001

# for i in range(2, x + 1):
#     d[i] = d[i - 1] + 1

#     if i % 2 == 0:
#         d[i] = min(d[i], d[i//2] + 1)

#     if i % 3 == 0:
#         d[i] = min(d[i], d[i//3] + 1)

#     if i % 5 == 0:
#         d[i] = min(d[i], d[i//5] + 1)

# print(d[x])

sys.setrecursionlimit(10**6)


def make_one(x):
    data = []
    if x == 1:
        return 0

    if d[x] != 0:
        return d[x]
    else:
        data.append(x-1)

        if x % 2 == 0:
            data.append(x//2)
        if x % 3 == 0:
            data.append(x//3)
        if x % 5 == 0:
            data.append(x//5)

        d[x] = min(d[i] if d[i] != 0 else make_one(i) for i in data) + 1
        return d[x]


print(make_one(x))
