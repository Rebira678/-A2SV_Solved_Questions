#https://www.hackerrank.com/challenges/python-power-mod-power/problem?isFullScreen=true
collection=[]
for i in range(3):
    n=input()
    collection.append(n)
print(pow(int(collection[0]),int(collection[1])))
print(pow(int(collection[0]),int(collection[1]),int(collection[2])))
