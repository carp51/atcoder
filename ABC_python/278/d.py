from collections import defaultdict

connect = defaultdict(int)

N = int(input())
A = list(map(int, input().split()))
Q = int(input())

second_flag = False
now_num = -10

for i in range(Q):
    q = list(map(int, input().split()))

    T = q[0]

    if T == 1:
        connect = defaultdict(int)
        second_flag = True
        now_num = q[1]
    elif T == 2:
        connect[q[1] - 1] += q[2]
    else:
        if second_flag:
            print(now_num + connect[q[1] - 1])
        else:
            print(A[q[1] - 1] + connect[q[1] - 1])