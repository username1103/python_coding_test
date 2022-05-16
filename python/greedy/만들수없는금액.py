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

# 그리디 알고리즘에 대표적인 예시 거스름돈의 경우
# 더 큰 금액의 동전을 작은 동전으로 만들어 낼 수 있기에 이용가능 한것
# 작은 단위의 동전으로 (target - 1)까지 만들 수 있지만 화폐단위가 target보다 커지는 경우
# target의 값을 만들 수 없음.

# 또는 주어진 동전을 모두 더한 값이상이 되면 만들 수 없음.
# 즉 , if 문으로 break가 아닌 모든 화폐단위를 다 거쳐서 for문이 끝나게되면, 주어진 동전의 합보다 큰 값이 라는 말이 됌.
# 따라서 만들 수 없음
