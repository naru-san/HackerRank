t=int(input().strip())
for i in range(0,t):
    n=int(input().strip())
    a=0
    b=0
    c=0
    if n//3==n/3:
        a=(n-1)//3
    else:
        a=n//3
    if n//5==n/5:
        b=(n-1)//5
    else:
        b=n//5
    if n//15==n/15:
        c=(n-1)//15
    else:
        c=n//15
    s=(a*(a+1)*3+b*(b+1)*5-c*(c+1)*15)//2
    print(s)
