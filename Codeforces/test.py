# s="appl"

# print(s)
# print(s[::-1])
# for i in range(len(s)//2):
#     print(s[i],end="")

# n=int(input())
# product=1
# for i in range(n):
#   product*=int(input())

# print(product)

# n,q,t=map(int,input().split())
# a=list(map(int,input().split()))
# prefix=[0]*(n)
# prefix[0]=a[0]
# for i in range(1,n):
#     prefix[i]=prefix[i-1]+a[i]
# for _ in range(q):
#     l,r=map(int,input().split())

#     if l == 1:
#         total = prefix[r - 1]
#     else:
#         total = prefix[r - 1] - prefix[l - 2] 
#     if total>t:
#         print("Yes")
#     else:
#         print("No")

n, k = map(int, input().split())
h = list(map(int, input().split()))

h.sort()
if k % 2 == 0:
    p = k // 2

    ans = sum(h[n-p:]) - sum(h[:p])

else:
    p = (k + 1) // 2

    ans = 2 * sum(h[n-p:]) - 2 * sum(h[:p-1])
    ans -= h[p-1] + h[p]

print(ans)



N, M = map(int, input().split())
P = list(map(int, input().split()))

parking = [False] * (M + 1)  
count = 0

for p in P:
    for j in range(p, M + 1):
        if not parking[j]:
            parking[j] = True
            count += 1
            break

print(count)