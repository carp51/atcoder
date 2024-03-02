def f(N, A):
    l_height = [0] * N
    r_height = [0] * N

    for i in range(N):
        if i == 0:
            l_height[i] = 1
        else:
            l_height[i] = min(l_height[i - 1] + 1, A[i])
    
    for i in range(N - 1, -1, -1):
        if i == N - 1:
            r_height[i] = 1
        else:
            r_height[i] = min(r_height[i + 1] + 1, A[i])
            
    max_size = 0
    for i in range(N):
        height = min(l_height[i], r_height[i])
        max_size = max(max_size, height)

    return max_size

N = int(input())
A = list(map(int, input().split()))
print(f(N, A))
