t=int(input())
for _ in range(t):
    symbol=input()
    n=len(symbol)

    if n%2==0 and symbol[0] !=')' and symbol[-1]!= "(":
        print("YES")
    else:
        print("NO")