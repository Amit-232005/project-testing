import sys
sys.setrecursionlimit(200000)

for _ in range (int(input())):
    def print_digit(n):
        if n==0:
            return
         
        print(n%10,end=" ")
        return print_digit(n//10)

    n=int(input())
    print(print_digit(n))
    

    

