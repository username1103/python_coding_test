import sys
input = sys.stdin.readline

n, c = map(int, input().split(' '))
houses = []
for _ in range(n):
    houses.append(int(input()))

houses.sort()


start = 1
end = houses[-1] - houses[0]
result = 0

while start <= end:
    select = (start + end) // 2
    count = 1
    value = houses[0]
    for i in range(1, n):
        if houses[i] >= value + select:
            value = houses[i]
            count += 1

    if count >= c:
        start = select + 1
        result = select
    else:
        end = select - 1

print(result)
