n=int(input())

def pyramid(n,i):
    if(i==0):
        return
    print(" " *(n-i) + "*" *(2*i-1))
    pyramid(n,i-1)

pyramid(n,n)