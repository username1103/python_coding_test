import sys

n = int(input())

# count_sort: 수 범위가 적을 때 유리함
counter = [0] * (10000+1)

for _ in range(n):
    counter[int(sys.stdin.readline().rstrip())] += 1

for i in range(1,len(counter)):
    for _ in range(counter[i]):
        print(i)
