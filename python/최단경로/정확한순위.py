# 6 6
# 1 5
# 3 4
# 4 2
# 4 6
# 5 2
# 5 4

n, m = map(int, input().split())  # 학생의 수와 비교 횟수 입력받기
INF = 500 * 500 + 1  # n이 500이하 이므로 다음과 같이 설정

data = [[INF] * n for _ in range(n)]  # 그래프 인접행렬 이용
# a에서 b로 가는 비용을 1로 설정
for _ in range(m):
    a, b = map(int, input().split())
    data[a - 1][b - 1] = 1

# 자기 자신에게 가는 비용을 0으로 설정
for i in range(n):
    data[i][i] = 0

# 플로이드 와샬 알고리즘을 수행
for k in range(n):
    for i in range(n):
        for j in range(n):
            data[i][j] = min(data[i][j], data[i][k] + data[k][j])

result = 0  # 정확한 순위를 알 수 있는 학생 수

# 각각의 학생에 대해 비교가능한 학생의 수 체크
for i in range(n):
    cnt = 0  # 비교가능한 학생수 체크
    for j in range(n):
        # 해당 값이 INF가 아니라면 비교가능한 것
        if data[i][j] != INF or data[j][i] != INF:
            cnt += 1
    # 해당 학생과 비교가능한 학생의 수가 n명이면 순위를 정확히 알 수 있는 것
    if cnt == n:
        result += 1

print(result)
