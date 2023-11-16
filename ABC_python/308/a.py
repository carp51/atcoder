S = list(map(int, input().split()))

for i in range(len(S) - 1):
    if not (S[i] % 25 == 0):
        print("No")
        exit()
    
    if not 100 <= S[i] <= 675:
        print("No")
        exit()
        
    if S[i + 1] < S[i]:
        print("No")
        exit()
        
if not S[-1] % 25 == 0:
    print("No")
    exit()
    
if not 100 <= S[-1] <= 675:
    print("No")
    exit()
    
print("Yes")