import sys
sys.setrecursionlimit(200000)

n=int(input())
a=list(map(int,input().split()))

i=0
def fun(a,n,i):
    if(i==n-1):
        return a[i]
    return max(a[i],fun(a,n,i+1))

print(fun(a,n,i))
