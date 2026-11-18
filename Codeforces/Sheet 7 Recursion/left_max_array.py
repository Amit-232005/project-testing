import sys
sys.setrecursionlimit(200000)

n = int(input())
a = list(map(int, input().split()))
arr=[a[0]]

def left_max(a,n,i):
    if i==n:
        return
    arr.append(max(arr[i-1],a[i]))
    return left_max(a,n,i+1)

left_max(a,n,1)
print(*arr)

    