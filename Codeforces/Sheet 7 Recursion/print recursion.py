n=int(input())

def recursion(n):
    if n==0:
        return 
    print("I love Recursion")
    return recursion(n-1)

recursion(n)