N = int(input())
S = input()
T = input()

tmp = 0

for i in range(N):
    if S[i] == T[i]:
        tmp += 1
    else:
        if (S[i] == "1" and T[i] == "l") or (S[i] == "l" and T[i] == "1"):
            tmp += 1
        
        if (S[i] == "0" and T[i] == "o") or (S[i] == "o" and T[i] == "0"):
            tmp += 1
                
print("Yes" if tmp == N else "No")