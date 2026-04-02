brackets=input()
n=len(brackets)

max_len=0
count=0
stack=[]
checker=[0]* n
for i in range(n):
    if brackets[i]==")":
        if stack:
            j=stack.pop()
            checker[i] = (checker[j-1] if j>0 else 0)+(i-j+1)
            if checker[i]>max_len:
                max_len=checker[i]
                count=1
            elif checker[i]==max_len:
                count+=1
    else:
        stack.append(i)

if max_len == 0:
    count = 1
    
print(max_len,count)