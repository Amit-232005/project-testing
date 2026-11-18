import sys
sys.setrecursionlimit(200000)



n,r=map(int,input().split())

# recursion
def combination(n,r):
    if n<r or n<0 or r<0:
        return 0
    if n==r or r==0:
        return 1
    if r==1:
        return n
    return combination(n-1,r-1)+combination(n-1,r)

print(combination(n,r))

# ncr=n-1cr-1+n-1cr

# # memoization
dp = [[-1] * (r+1)  for _ in range(n+1)]

def memo(n,r,dp):
    if n<r or n<0 or r<0:
        return 0
    if n==r or r==0:
        return 1
    if r==1:
        return n
    if dp[n][r]!=-1:
        return dp[n][r]
    dp[n][r]= memo(n-1,r-1,dp)+memo(n-1,r,dp)
    return dp[n][r]

print(memo(n,r,dp))

# tabulation
dp1=[[0]*(r+1) for _ in range(n+1)]

for i in range(n+1):
    dp1[i][0]=1

for i in range(1,n+1):
    for j in range(1,r+1):
        dp1[i][j]=dp1[i-1][j]+dp1[i-1][j-1]

print(dp1[n][r])
