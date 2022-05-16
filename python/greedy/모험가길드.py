# 5
# 2 3 1 2 2
n = int(input())

data = sorted(list(map(int, input().split())))

result = 0  # 그룹 수
count = 0  # 그룹인원 체크

for i in data:
    # 그룹인원 추가
    count += 1
    # 그룹의 인원이 공포도 보다 같거나 높으면
    if count >= i:
        result += 1  # 그룹의 포함
        count = 0  # 그룹인원 초기화

print(result)
