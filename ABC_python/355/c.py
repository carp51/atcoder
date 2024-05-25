N, T = map(int, input().split())
A = list(map(int, input().split()))

retu_list = [0 for _ in range(N)]
gyou_list = [0 for _ in range(N)]
naname_list = [0, 0]

l_naname = set([i * N + (i + 1) for i in range(N)])
r_naname = set([(i + 1) * N - i for i in range(N)])

for i in range(T):
    gyou_list[(A[i] - 1) // N] += 1
    retu_list[(A[i] - 1) % N] += 1
    if A[i] in l_naname:
        naname_list[0] += 1
        
    if A[i] in r_naname:
        naname_list[1] += 1
        
    if gyou_list[(A[i] - 1) // N] == N or retu_list[(A[i] - 1) % N] == N or naname_list[0] == N or naname_list[1] == N:
        print(i + 1)
        exit()
        
print(-1)