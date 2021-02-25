import heapq

food_times = [3, 1, 2]
k = 5


def solution(food_times, k):
    # 먹을 음식의 총 양이 k보다 작다면 => 즉 먹을 음식이 부족하게 됨
    if sum(food_times) <= k:
        return -1

    q = []  # 현재 남아있는 음식들을 담음 (초기양, 음식번호) | 초기양에 따라 오름차순 정렬
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))

    sum_value = 0  # 전체시간
    previous = 0  # 이전 음식의 초기 양
    length = len(food_times)  # 현재 남은 음식 종류

    # 남아있는 음식들중 먹는데 가장 적은 시간이 걸리는 음식이 현재 남은 양만큼 전체음식을 먹었을때 까지 걸린 전체시간이 k보다 작거나 같다면 진행
    # q에는 음식의 양에 따라 오름차순 정렬되어 있고, previous는 초기양이 가장 적은 음식부터 나오므로 q[0][0] - previous 는 남은 음식의 현재 남은 양을 나타냄
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]  # 남은 음식중 먹는데 걸리는 시간이 가장 적게 걸리는 음식을 제거
        sum_value += (now - previous) * length  # 나머지 전체음식 식사
        length -= 1  # 가장 적게걸리는 음식을 제거했으므로 남은 음식 종류 1감소
        previous = now  # 이전 음식의 초기 양

    # 남은 음식들을 번호순으로 재정렬
    result = sorted(q, key=lambda x: x[1])
    # k에서 지금까지 음식을 먹는데 걸린시간을 빼주고 length로 나눠주어 먹어야 하는 음식 출력
    return result[(k - sum_value) % length][1]


print(solution(food_times, k))
