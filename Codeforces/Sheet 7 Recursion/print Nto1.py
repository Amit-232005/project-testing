n=int(input())

def print_num(n):
    if n==0:
        return 
    print(n,end=" ")
    return print_num(n-1)

print_num(n)