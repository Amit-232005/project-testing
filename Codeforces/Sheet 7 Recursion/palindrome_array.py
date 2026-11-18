import sys
sys.setrecursionlimit(500000)

n=int(input())
a=list(map(int,input().split()))

def palindrome(a,i,n):
    if i>=n//2:
        return True
    if a[i]!=a[n-1-i]:
        return False
    return palindrome(a,i+1,n)

flag=palindrome(a,0,n)

if flag:
    print("YES")
else:
    print("NO")