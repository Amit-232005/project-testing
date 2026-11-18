import sys
sys.setrecursionlimit(200000)

n= int(input())
a = list(map(int, input().split()))

def summation(a, i, n):
    if i == n:
        return 0
    return a[i] + summation(a, i + 1, n)

print( format(summation(a, 0, n)/n,".6f"))