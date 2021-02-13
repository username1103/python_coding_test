# BaekJoon 2110
# 도현이의 집 N개가 수직선 위에 있다. 각각의 집의 좌표는 x1, ..., xN이고, 집 여러개가 같은 좌표를 가지는 일은 없다.

# 도현이는 언제 어디서나 와이파이를 즐기기 위해서 집에 공유기 C개를 설치하려고 한다.
# 최대한 많은 곳에서 와이파이를 사용하려고 하기 때문에, 한 집에는 공유기를 하나만 설치할 수 있고,
# 가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치하려고 한다.

# C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 집의 개수 N (2 ≤ N ≤ 200,000)과 공유기의 개수 C (2 ≤ C ≤ N)이 하나 이상의 빈 칸을 사이에 두고 주어진다.
# 둘째 줄부터 N개의 줄에는 집의 좌표를 나타내는 xi (0 ≤ xi ≤ 1,000,000,000)가 한 줄에 하나씩 주어진다.

# 출력
# 첫째 줄에 가장 인접한 두 공유기 사이의 최대 거리를 출력한다.

# 5 3
# 1
# 2
# 8
# 4
# 9

# 3

import sys
input = sys.stdin.readline

# 집의 개수와 공유기의 개수 입력받기
n, c = map(int, input().split(' '))

# 집의 좌표를 입력받음
houses = []
for _ in range(n):
    houses.append(int(input()))

# 좌표순으로 오름차순 정렬
houses.sort()

# 간격을 기준으로 이진탐색 수행
start = 1
end = houses[-1] - houses[0]
result = 0

# 이진탐색 수행
while start <= end:

    select = (start + end) // 2
    count = 1  # 공유기의 개수
    value = houses[0]  # 첫 집에 설치

    # 첫 집 이후부터 정해진 간격 이후에 가장 가까운 집들에게 공유기 설치
    for i in range(1, n):
        if houses[i] >= value + select:
            value = houses[i]
            count += 1

    # 공유기 개수가 목표치인 c보다 크거나 같을 경우
    # 해당 답을 저장하고 다시 진행
    if count >= c:
        start = select + 1
        result = select
    # 목표치보다 작을 경우 end를 땡겨와서 간격 조정
    else:
        end = select - 1

print(result)
