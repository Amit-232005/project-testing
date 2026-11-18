for _ in range(int(input())):
    def fun(n):
        if n == 1:
            return True

        if n % 10 != 0:
            return False

        if fun(n // 10):
            return True

        if n % 20 == 0:
            return fun(n // 20)

        return False

    n = int(input())

    if fun(n):
        print("YES")
    else:
        print("NO")