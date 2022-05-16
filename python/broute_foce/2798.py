import itertools

n,m = map(int, input().split())
values = list(map(int,input().split()))

candidate = list(itertools.combinations(values,3))

sum_result = list(map(sum, candidate))

max = 0
for x in sum_result:
    if x > max and x <= m:
        max = x
    if max == m:
        break

print(max)


