#
#https://codeforces.com/problemset/problem/1605/C

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()

    ans = -1

    # length 2
    for i in range(n - 1):
        a = b = c = 0
        for j in range(i, i + 2):
            if s[j] == 'a':
                a += 1
            elif s[j] == 'b':
                b += 1
            else:
                c += 1

        if a > b and a > c:
            ans = 2
            break

    # length 3
    if ans == -1:
        for i in range(n - 2):
            a = b = c = 0
            for j in range(i, i + 3):
                if s[j] == 'a':
                    a += 1
                elif s[j] == 'b':
                    b += 1
                else:
                    c += 1

            if a > b and a > c:
                ans = 3
                break

    # length 4
    if ans == -1:
        for i in range(n - 3):
            a = b = c = 0
            for j in range(i, i + 4):
                if s[j] == 'a':
                    a += 1
                elif s[j] == 'b':
                    b += 1
                else:
                    c += 1

            if a > b and a > c:
                ans = 4
                break

    # length 7
    if ans == -1:
        for i in range(n - 6):
            a = b = c = 0
            for j in range(i, i + 7):
                if s[j] == 'a':
                    a += 1
                elif s[j] == 'b':
                    b += 1
                else:
                    c += 1

            if a > b and a > c:
                ans = 7
                break

    print(ans)
