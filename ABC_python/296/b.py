S = [list(input()) for i in range(8)]

for i in range(8):
    for j in range(len(S[i])):
        if S[i][j] == "*":
            ans = str(chr(j + 97)) + str(8 - i)
            
            print(ans)
            exit()