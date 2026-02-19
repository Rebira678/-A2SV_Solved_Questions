#B. Polycarp Training
#https://codeforces.com/problemset/problem/1165/B
n=int(input())
questions=list(map(int,input().split()))
questions.sort()
days=0
checker=1
for i in questions:
    if checker<=i:
        days+=1
        checker+=1

print(days)
