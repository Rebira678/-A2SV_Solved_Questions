#https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true
def swap_case(s):
    m=list(s)
    for i in range(len(m)):
        if m[i]==m[i].lower():
            m[i]=m[i].upper()
        elif m[i]==m[i].upper():
            m[i]=m[i].lower()    
    return "".join(m)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
