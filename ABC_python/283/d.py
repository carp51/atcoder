from collections import defaultdict


S = input()
N = len(S)

check = defaultdict(int)
connected = [0 for _ in range(N + 10)]


for i in range(N):
    if S[i] == "(":
        continue
    elif S[i] == ")":
        count = 1
        cnt = i
        while count != 0:
            cnt -= 1
            if S[cnt] == ")":
                count += 1
            elif S[cnt] == "(":
                count -= 1
            if connected[cnt] == 0:
                check[S[cnt]] -= 1
                connected[cnt] = -1

    else:
        if check[S[i]] != 0:
            print("No")
            exit()

        check[S[i]] += 1

print("Yes")