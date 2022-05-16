n = int(input())

count = 1
initValue = 666
value = initValue

while count < n:
    value += 1
    if str(value).find('666') != -1:
        count += 1

print(value)