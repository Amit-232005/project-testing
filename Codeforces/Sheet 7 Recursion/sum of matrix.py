r,c=map(int,input().split())
a = []
b = []

for i in range(r):
    row = list(map(int, input().split()))
    a.append(row)

# for i in range(r):
#     row = list(map(int, input().split()))
#     b.append(row)

sum=0
print(i)

# def matrix_sum(a,b,sum,i,j):
#     if i==r and j==c:
#         return sum
#     sum+=(a[i][j]+b[i][j])
#     i+=1
#     j+=1
#     return sum+matrix_sum(a,b,sum,i,j)

# print(matrix_sum(a,b,sum,0,0))



# 4 3
# 1 2 3
# 4 5 6
# 1 3 5