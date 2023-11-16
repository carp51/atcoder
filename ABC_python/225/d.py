N, Q = map(int, input().split())

check = [[-10, -10] for _ in range(N + 10)]

for i in range(Q):
    q = list(map(int, input().split()))

    if q[0] == 1:
        x, y = q[1], q[2]
        check[x][1] = y
        check[y][0] = x
    elif q[0] == 2:
        x, y = q[1], q[2]
        check[x][1] = -10
        check[y][0] = -10
    else:
        ans = []
        start = q[1]

        while check[start][0] != -10:
            start = check[start][0]

        while check[start][1] != -10:
            ans.append(start)
            start = check[start][1]

        ans.append(start)

        print(len(ans), *ans)       
