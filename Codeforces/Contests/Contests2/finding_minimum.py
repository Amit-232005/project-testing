n, k = map(int, input().split())
arr = list(map(int, input().split()))

ans = []

for i in range(0, n, k):
    mini = arr[i]

    for j in range(i, min(i + k, n)):
        mini = min(mini, arr[j])

    ans.append(mini)

print(*ans)