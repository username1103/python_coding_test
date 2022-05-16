n = int(input())

value = []
for _ in range(n):
    value.append(int(input()))

# 기본이 오름차순 정렬
value.sort()

print(*value, sep="\n")