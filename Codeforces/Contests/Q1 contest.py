for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))

    count=l.count(0)
    if l[0]==0 and l[n-1]==0:
        print(0)
    if (l[0]==0 and l[n-1]==1) or (l[0]==1 and  l[n-1]==0) :
        if(count>=2):
            print(1)
        else:
            print(-1)
    if l[0]==1 and l[n-1]==1:
        if(count>=2):
            print(2)
        else:
            print(-1)