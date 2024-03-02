S = input()

ans = 0

count = 0

for i in range(len(S)):
    ans += 1
    if S[i] == "0":
        count += 1
    else:
        count = 0

    if count == 2:
        ans -= 1
        count = 0

print(ans)
