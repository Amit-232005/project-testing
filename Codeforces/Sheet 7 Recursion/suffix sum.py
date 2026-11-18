n,m=map(int,input().split())
a=list(map(int,input().split()))


def suffix_sum(a,n,i):
    if i==n:
        return 0
    i+=1
    return a[i]+summation(a,n,i)

print (suffix_sum(a,n,n-m))
