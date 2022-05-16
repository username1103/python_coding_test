n = int(input())

result = 0
for i in range(n,0,-1):
    values = list(map(int,str(i)))
    if i + sum(values) == n:
        result = i

print(result)