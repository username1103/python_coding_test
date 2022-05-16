n = int(input())

values = []
for _  in range(n):
    x,y = list(map(int,input().split()))
    values.append([x,y])


result = []

for x,y in values:
    count = 1;
    for x2,y2 in values:
        if x2 > x and y2 > y:
            count += 1;
    result.append(count)

print(*result, sep=' ')

