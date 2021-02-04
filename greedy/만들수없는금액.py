# 5
# 3 2 1 1 9

n = int(input())
money = sorted(list(map(int, input().split())))

target = 1

# 누적합과 화폐단위를 비교하면서 화폐단위가 누적합 보다 큰 경우, 두 수 사이에 갭이 존재한다는 뜻. 따라서 중간에 만들지 못하는 금액이 발생.
for x in money:
    if target < x:
        break
    target += x

print(target)
