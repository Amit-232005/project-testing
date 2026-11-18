import sys
sys.setrecursionlimit(500000)

n=int(input())
def log2(n):
    if n==1:
        return 0
    return 1+log2(n//2)

print(log2(n))