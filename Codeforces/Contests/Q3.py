for _ in range(int(input())):
    x,y=map(int,input().split())

    ans=float ('-inf')
    xor=x^y
    ops=0
    while x>0 and y>0:
        if x>0:
            x-=1
            y+=1
            xor=x^y
            ops+=1 
        elif y>0:
            y-=1
            x+=1
            xor=x^y
            ops+=1
    ans=max(ans,xor)
    
    print(ans,ops)
