# s,e=map(int,input().split())

# # def ways(s,e):
# #     if s==e:
# #         return 1
# #     if s>e:
# #         return 0
# #     return ways(s+1,e) + ways(s+2,e) + ways(s+3,e)
# # print(ways(s,e))

# other ques
# given a number n, divide it by 2 or 3, find total no. of ways  to reach 0
n=400
cnt=0


def ways(n):
    global cnt
    cnt+=1
    if(n==0):
        return 1    
    return ways(n//2)+ways(n//3)

# memoization
dp=[-1]*(n+1)
cnt_dp=0

def ways_dp(n):
    global cnt_dp
    cnt_dp+=1
    if(n==0):
        return 1
    if dp[n]!=-1:
        return dp[n]
    dp[n]=ways_dp(n//2) +ways_dp(n//3)
    return dp[n]
    


print(ways(n))
print("No. of calls without dp=",cnt)
print(ways_dp(n))
print("No. of calls with dp=",cnt_dp)


# tabulation
dp1=[-1]*(n+1)
cnt_dp1=0

dp1[0]=1


def ways_dp1(n):
    global cnt_dp1
    cnt_dp1+=1
    for i in range(1,n+1):
        dp1[i]=dp1[i//2]+dp1[i//3]
    return dp1[n]

print("tabulation:",ways_dp1(n))