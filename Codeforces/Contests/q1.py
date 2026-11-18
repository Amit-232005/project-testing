for _ in range(int(input())):
    n,k=map(int,input().split())
    s=input()

    count=0
    for i in range(0,n,k):
        farm=s[i:k+i]
        if '0' not in farm:
            count+=1
    print(count)
