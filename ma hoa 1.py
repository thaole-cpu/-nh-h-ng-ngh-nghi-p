for t in range(int(input())):
    s = input()
    s = s + ' '
    cnt = 1
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            cnt += 1
        else:
            print(cnt, s[i], sep='', end='')
            cnt = 1
    print()


