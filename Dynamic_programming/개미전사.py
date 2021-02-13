# 4
# 1 3 1 5

n = int(input())  # 식량창고의 개수
data = list(map(int, input().split()))  # 식량창고에 저장된 식량의 개수
d = [0] * n  # 메모제이션을 위한 list

d[0] = data[0]
d[1] = max(data[0], data[1])

for i in range(2, n):
    # 이전 식량 창고 까지 털었을 경우와 2개 전 식량창고까지 털고 이번 식량창고를 터는 경우 중 큰 쪽을 선택
    d[i] = max(d[i - 1], d[i - 2] + data[i])

print(d[n - 1])
