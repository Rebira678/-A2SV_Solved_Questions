#https://codeforces.com/contest/263/problem/A
#
matrix=[]
count=0
for i in range(5):
    row=list(map(int,input().split()))
    matrix.append(row)
for i in range(5):
    for j in range(5):
        if matrix[i][j]==1:
            count=abs(i-2)+abs(j-2)
print(count)
