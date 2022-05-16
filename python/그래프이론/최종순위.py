# BaekJoon 3665
# 올해 ACM-ICPC 대전 인터넷 예선에는 총 n개의 팀이 참가했다. 팀은 1번부터 n번까지 번호가 매겨져 있다.
# 놀랍게도 올해 참가하는 팀은 작년에 참가했던 팀과 동일하다.

# 올해는 인터넷 예선 본부에서는 최종 순위를 발표하지 않기로 했다. 그 대신에 작년에 비해서 상대적인 순위가 바뀐 팀의 목록만 발표하려고 한다.
# (작년에는 순위를 발표했다) 예를 들어, 작년에 팀 13이 팀 6 보다 순위가 높았는데, 올해 팀 6이 팀 13보다 순위가 높다면, (6, 13)을 발표할 것이다.

# 창영이는 이 정보만을 가지고 올해 최종 순위를 만들어보려고 한다. 작년 순위와 상대적인 순위가 바뀐 모든 팀의 목록이 주어졌을 때,
# 올해 순위를 만드는 프로그램을 작성하시오. 하지만, 본부에서 발표한 정보를 가지고 확실한 올해 순위를 만들 수 없는 경우가 있을 수도 있고,
# 일관성이 없는 잘못된 정보일 수도 있다. 이 두 경우도 모두 찾아내야 한다.

# 입력
# 첫째 줄에는 테스트 케이스의 개수가 주어진다. 테스트 케이스는 100개를 넘지 않는다.
# 각 테스트 케이스는 다음과 같이 이루어져 있다.

# 팀의 수 n을 포함하고 있는 한 줄. (2 ≤ n ≤ 500)
# n개의 정수 ti를 포함하고 있는 한 줄. (1 ≤ ti ≤ n) ti는 작년에 i등을 한 팀의 번호이다. 1등이 가장 성적이 높은 팀이다. 모든 ti는 서로 다르다.
# 상대적인 등수가 바뀐 쌍의 수 m (0 ≤ m ≤ 25000)
# 두 정수 ai와 bi를 포함하고 있는 m줄. (1 ≤ ai < bi ≤ n) 상대적인 등수가 바뀐 두 팀이 주어진다. 같은 쌍이 여러 번 발표되는 경우는 없다.
# 출력
# 각 테스트 케이스에 대해서 다음을 출력한다.

# n개의 정수를 한 줄에 출력한다. 출력하는 숫자는 올해 순위이며, 1등팀부터 순서대로 출력한다.
# 만약, 확실한 순위를 찾을 수 없다면 "?"를 출력한다. 데이터에 일관성이 없어서 순위를 정할 수 없는 경우에는 "IMPOSSIBLE"을 출력한다.

# 3
# 5
# 5 4 3 2 1
# 2
# 2 4
# 3 4
# 3
# 2 3 1
# 0
# 4
# 1 2 3 4
# 3
# 1 2
# 3 4
# 2 3

# 5 3 2 4 1
# 2 3 1
# IMPOSSIBLE


from collections import deque
import sys
input = sys.stdin.readline


# 테스트 횟수 입력받기
t = int(input())
# 테스트 진행
for _ in range(t):
    # 팀 수 입력받기
    n = int(input())

    # 지난해 등수 입력받기
    last_year = list(map(int, input().split()))
    # 각 팀의 차수 테이블
    indegree = [0] * (n + 1)

    # 높은 등수에서 낮은 등수의 팀으로 간선 연결
    graph = [[] for _ in range(n + 1)]
    for i in range(n):
        for j in range(i+1, n, 1):
            graph[last_year[i]].append(last_year[j])
            indegree[last_year[j]] += 1

    # 순위가 변동된 횟수 입력 받기
    m = int(input())

    # 순위가 변경되는 경우 처리
    for _ in range(m):
        a, b = map(int, input().split())
        # b가 a보다 높은 등수 였다면
        if a in graph[b]:
            # a에서 b로 가는 간선을 추가 & b에서 a로 가는 간선 제거 & 그에 따른 차수 조정
            graph[a].append(b)
            indegree[b] += 1
            indegree[a] -= 1
            if a in graph[b]:
                graph[b].remove(a)
        # a가 b보다 높은 등수 였다면
        else:
            # b에서 a로 가는 간선 추가 & a에서 b로 가는 간선 제거 & 그에 따른 차수 조정
            graph[b].append(a)
            indegree[a] += 1
            indegree[b] -= 1
            if b in graph[a]:
                graph[a].remove(b)

    # 위상정렬을 위한 큐 생성
    q = deque()
    # 차수가 0인 팀. 즉 순위가 가장 높은 팀을 큐에 삽입
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    result = []  # 등수 결과 저장 리스트
    certain = True  # 등수가 명확한지 여부
    isImpossible = False  # 데이터의 일관성이 없는지 여부
    for i in range(n):
        if len(q) == 0:  # len(q) == 0 이라면 싸이클이 발생. 즉 데이터가 문제에서 제공하는 정보와 일치하지 않음.
            isImpossible = True
            break
        if len(q) == 1:  # 정확히 한팀이 명확하게 존재하는 경우
            now = q.pop()
            result.append(now)
            for node in graph[now]:
                indegree[node] -= 1
                if indegree[node] == 0:
                    q.appendleft(node)
        else:  # 차수가 0인팀 즉 가장 높은 순위의 팀이 2팀 이상 존재한다면, 확실한 순위를 찾을 수 없음
            certain = False
            break

    # 위에서 나온 결과에 따른 출력
    if isImpossible:
        print("IMPOSSIBLE")
    elif certain:
        for i in result:
            print(i, end=" ")
        print()
    else:
        print('?')
