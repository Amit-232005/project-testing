n=int(input())

def print_num(n,i):
    if i==n+1:
        return 
    print(i)
    return print_num(n,i+1)

print_num(n,1)