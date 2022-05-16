# 5 3
# 1 3 2 3 2

# 8 5
# 1 5 4 3 2 4 5 2

n, m = map(int, input().split())
ball = list(map(int, input().split()))

# 볼링공의 무게별 개수 담기
array = [0] * 11
for i in ball:
    array[i] += 1

cnt = 0
for i in range(1, m + 1):
    n -= array[i]  # 무게가 i인 볼링공 개수 제외 => 중복도 알아서 제거 됨
    cnt += array[i] * n  # 무게가 i인 볼링공 고르고 나머지 볼링공을 고르는 경우의 수

print(cnt)
