# for _ in range(int(input())):
#     x,y,k=(map(int,input().split()))
#     ans=0
#     for i in range(k):
#         ans+=(y+i)%(x+i) 
#     print(ans)
for _ in range(int(input())):
    x, y, k = map(int, input().split())

    d = y - x
    ans = 0

    limit = max(0, min(k, d - x + 1))

    for i in range(limit):
        ans += d % (x + i)

    # Remaining terms are simply d
    ans += (k - limit) * d

    print(ans)