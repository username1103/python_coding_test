# 3
n = int(input())  # 바닥의 가로 길이

d = [0] * n  # 메모제이션을 위한 list

# 초기화
d[0] = 1
d[1] = 3

# 바텀업 방식
for i in range(2, n):
    # 이전 길이 까지 채우는 방식에 단순히 2*1의 판을 추가한경우 + 전전 길이 까지 채우는 방식에 1*2 2개 또는 2*2 1개로 채우는 경우
    d[i] = (d[i - 1] + 2 * d[i - 2]) % 796796

print(d[n - 1])
