# 2
# 3 4
# 1 3 3 2 2 1 4 1 0 6 4 7
# 4 4
# 1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2


t = int(input())  # 횟수 입력받기

for _ in range(t):
    n, m = map(int, input().split())  # 금광의 크기 입력받기
    cave = list(map(int, input().split()))  # 금광 입력받기

    d = [0] * (m * n)  # dp테이블: 해당위치까지 캐서 올수 있는 최대 금의 양

    # dp테이블 첫 열 초기화
    for i in range(n):
        d[i * m] = cave[i * m]

    # 1열 부터 시작해서 왼쪽, 왼쪽위, 왼쪽아래에 값들이 존재한다면 그 값들중 최대값을 찾아 현재 값과 더하여
    # 값을 dp테이블에 저장
    for j in range(1, m):
        for i in range(n):
            temp = []
            temp.append(d[i * m + (j - 1)])
            if i - 1 >= 0:
                temp.append(d[(i - 1)*m + (j - 1)])
            if i + 1 < n:
                temp.append(d[(i + 1) * m + (j - 1)])
            d[i * m + j] = max(temp) + cave[i * m + j]

    # 마지막열중 가장 큰값 으로 result 갱신
    result = 0
    for i in range(n):
        result = max(result, d[i * m + (m - 1)])

    print(result)
