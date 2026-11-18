# n=int(input())
n=5
cnt=0

def fibo(n):
    global cnt+=1
    if n==1:
        return 0
    if n==2:
        return 1
    return fibo(n-1)+fibo(n-2)

print(fibo(n))
print(cnt)
