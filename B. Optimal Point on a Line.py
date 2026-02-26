#B. Optimal Point on a Line
#https://codeforces.com/contest/710/problem/B
n=int(input())
cordinates=list(map(int,input().split()))

cordinates.sort()
if n % 2==1:
    print (cordinates[int(n/2)])
else:
    print (cordinates[int(n//2)-1])
