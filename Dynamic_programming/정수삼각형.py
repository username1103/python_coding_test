# BaekJoon 1932
#         7
#       3   8
#     8   1   0
#   2   7   4   4
# 4   5   2   6   5
# 위 그림은 크기가 5인 정수 삼각형의 한 모습이다.

# 맨 위층 7부터 시작해서 아래에 있는 수 중 하나를 선택하여 아래층으로 내려올 때,
# 이제까지 선택된 수의 합이 최대가 되는 경로를 구하는 프로그램을 작성하라.
# 아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중에서만 선택할 수 있다.

# 삼각형의 크기는 1 이상 500 이하이다. 삼각형을 이루고 있는 각 수는 모두 정수이며, 범위는 0 이상 9999 이하이다.

# 입력
# 첫째 줄에 삼각형의 크기 n(1 ≤ n ≤ 500)이 주어지고, 둘째 줄부터 n+1번째 줄까지 정수 삼각형이 주어진다.

# 출력
# 첫째 줄에 합이 최대가 되는 경로에 있는 수의 합을 출력한다.


n = int(input())  # 삼각형의 크기

# 삼각형 입력 받기
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

# dp 테이블 : 해당 값까지 왔을 때 최댓 값
d = [[0] * i for i in range(1, n + 1)]
d[0][0] = data[0][0]  # dp 테이블 초기화

result = 0

# 해당 값이 처음 값인지 끝 값인지 중간 값인지 확인하여 최댓값을 설정
for i in range(1, len(data)):
    for j in range(len(data[i])):
        if j == 0:
            d[i][j] = d[i-1][j] + data[i][j]
        elif j == len(data[i]) - 1:
            d[i][j] = d[i-1][j-1] + data[i][j]
        else:
            d[i][j] = max(d[i-1][j] + data[i][j], d[i-1][j-1] + data[i][j])

        # 마지막줄에 도달하면 result값을 최댓값으로 갱신
        if i == len(data) - 1:
            result = max(result, d[i][j])

print(max(d[n-1]))
