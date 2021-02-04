# 5
# 2 3 1 2 2
n = int(input())

data = sorted(list(map(int, input().split())))

result = 0

for i in range(max(data)):
    cnt = data.count(i)
    if cnt != 0:
        result += (cnt // i)

print(result)
