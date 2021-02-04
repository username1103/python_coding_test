# 02984
# 567
n = list(map(int, input()))

result = 0
for num in n:
    if result == 0 or num == 0:
        result += num
    else:
        result *= num

print(result)
