# K1KA5CB7

# AJDKLSI412K4JSJ9D

n = input()

num = 0
string = ""
for i in n:
    if i.isdigit():
        num += int(i)
    else:
        string += i

print(''.join(sorted(string)), str(num))
