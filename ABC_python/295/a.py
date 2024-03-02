w = ["and", "not", "that", "the", "you"]

N = int(input())
W = list(map(str, input().split()))

for i in range(N):
    if W[i] in w:
        print("Yes")
        exit()
        
print("No")