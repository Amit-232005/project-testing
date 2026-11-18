# for _ in range (int(input())):

#     def fun(n,m):
#         if m >n :
#             return False
#         if m==n:
#             return True
#         return fun(n,m*10) or fun(n,m*20)

#     n=int(input())
#     if(fun(n,1)):
#         print("YES")
#     else:
#         print("NO")

# memoization 
# using dictionary
# for _ in range (int(input())):
#     dp={}

#     def fun(target,n):
#         if n>target:
#             return False
#         if n==target:
#             return True
#         if n in dp:
#             return dp[n]
#         dp[n]=fun(target,n*10) or fun(target,n*20)
#         return dp[n]

#     target=int(input())
#     print("YES" if fun(target,1) else "NO")

# tabulation
for _ in range (int(input())):
    dp={}
    dp[1]=True
    target=int(input())
    
    for i in range (1,target+1):
        if i==target:
            dp[i]=True
        if i>target:
            dp[i]= False
        if i in dp:
            print(dp[i]) 
        dp[i]=dp[i-1]*10 or dp[i-1]*20
        
    print("YES" if dp[target] else "NO")
        