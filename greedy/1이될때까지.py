# 25 5

n, k = list(map(int, input().split()))

cnt = 0

while True:

    temp = (n // k) * k
    cnt += (n - temp)
    n = temp

    if n < k:
        break

    cnt += 1
    n //= k

cnt += (n - 1)
print(cnt)
