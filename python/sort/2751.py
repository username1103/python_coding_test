import sys

n = int(input())

value = []
for _ in range(n):
    # sys.stdin.readline().rstip()이 input()보다 빠르다.
    value.append(int(sys.stdin.readline().rstrip()))


value.sort()

print(*value, sep="\n")