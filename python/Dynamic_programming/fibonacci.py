# 아래와 같이 작성할 경우, n이 커지면 계산량이 기하 급수적으로 늘어나게 되는 문제가 있음
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x - 1) + fibo(x - 2)


# 메모제이션 기법을 이용한 피보나치 수열
d = [0] * 100


def fibo_memo(x):
    if x == 1 or x == 2:
        return 1

    if d[x] != 0:
        return d[x]

    d[x] = fibo_memo(x - 1) + fibo_memo(x - 2)
    return d[x]


# 반복문을 이용한 피보나치 수열
d[1] = 1
d[2] = 1
n = 99

for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]

print(d[n])


# print(fibo(4))
# print(fibo_memo(99))
