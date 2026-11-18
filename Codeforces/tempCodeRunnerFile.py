n,q,t=map(int,input().split())
a=list(map(int,input().split()))
for _ in range(q):
    l,r=map(int,input().split())
    sum=0
    for i in range(l-1,r):
        sum+=a[i]
    if sum>t:
        print("YES")
    else:
        print("NO")