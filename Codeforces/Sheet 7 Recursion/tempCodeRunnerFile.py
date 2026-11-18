
# # memoization
# dp = [[-1] * r  for _ in range(n)]

# def memo(n,r,dp):
#     if n<r or n<0 or r<0:
#         return 0
#     if n==r or r==0:
#         return 1
#     if r==1:
#         return n
#     if dp[n-1][r-1]!=-1:
#         return dp[n-1][r-1]
#     dp[n-1][r-1]= memo(n-1,r-1,dp)+memo(n-1,r,dp)
#     return dp[n-1][r-1]

# print(memo(n,r,dp))
