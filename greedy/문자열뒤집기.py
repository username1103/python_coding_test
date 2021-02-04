# 0001100

s = list(map(int, input()))

cnt = 0
end = 0

if s[0] == s[-1]:
    main = s[0]
    while True:
        try:
            start = s.index((main+1) % 2, end)
            end = s.index(main, start + 1)
            cnt += 1
        except:
            break
else:
    main = s[-1]
    while True:
        try:
            start = s.index((main+1) % 2, end)
            end = s.index(main, start + 1)
            cnt += 1
        except:
            break


print(cnt)
