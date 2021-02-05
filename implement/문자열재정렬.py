# K1KA5CB7

# AJDKLSI412K4JSJ9D

n = input()

n = ''.join(sorted(n))

total = 0
index = 0
for i in range(len(n)):
    if n[i].isdigit():
        total += int(n[i])
    else:
        index = i
        break

print(n[index:], total, sep="")
