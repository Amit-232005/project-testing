import sys
sys.setrecursionlimit(200000)

n=int(input())
a=list(map(int,input().split()))

def even_indices(a,i):
    if i==-1:
        return
    if i%2==0:
        print(a[i],end=" ")
    return even_indices(a,i-1)

even_indices(a,n-1)