def f(n):
    if n == 1:
        return 1

    return f(n // 2) + f(-(-n // 2))

N = int(input())


print(f(N))