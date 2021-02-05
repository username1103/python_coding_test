# 123402

# 7755
n = input()

front = n[:len(n)//2]
end = n[len(n)//2:]

val1 = 0
val2 = 0
for data in front:
    val1 += int(data)

for data in end:
    val2 += int(data)

if val1 == val2:
    print("LUCKY")
else:
    print("READY")
