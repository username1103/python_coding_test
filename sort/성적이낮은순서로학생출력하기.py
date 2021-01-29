# 2
# 홍길동 95
# 이순신 77

def setting(data):
    return data[1]


n = int(input())
data = []
for _ in range(n):
    input_data = input().split()
    data.append((input_data[0], input_data[1]))

data.sort(key=setting)

for i in range(n):
    print(data[i][0], end=" ")
