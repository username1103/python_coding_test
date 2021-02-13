# 2 15
# 2
# 3

# 3 4
# 3
# 5
# 7

n, m = map(int, input().split())  # 화폐의 개수와 목표 금액

# 화폐 리스트 받기
data = []
for i in range(n):
    data.append(int(input()))

# 메모제이션을 위한 lsit
d = [10001] * (m + 1)
d[0] = 0

# 내 풀이

for i in range(1, m + 1):
    # 여러 화폐들 중  현재 금액에서 각각의 화폐를 뺀 금액 리스트 생성
    temp = [i - j for j in data if i - j >= 0]
    if not temp:
        continue
    # 각각의 화폐를 뺀 금액들까지 도달하기위한 화폐 구성중 가장 적은 수의 구성에 + 1 로 갱신
    d[i] = min(d[k] for k in temp) + 1

# 답지 풀이

# for i in range(n): # 모든 화폐들에 대해서
#     for j in range(data[i], m + 1): # 각각의 화폐 단위 이후 부터 금액들에 대해서 갱신
#         if d[j - data[i]] != 10001:  # 없어도 되는 부분 b/c 어차피 d[j -data[i]] 가 10001이 더라도 항상 d[j]값을 반환하기 때문에
#             d[j] = min(d[j - data[i]] + 1, d[j]) # 현재 값과 특정 화폐를 뺀 금액까지의 구성 + 1 의 개수를 비교하여 작은 값으로 갱신

if d[m] >= 10001:
    print(-1)
else:
    print(d[m])
