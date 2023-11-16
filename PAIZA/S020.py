N = int(input())
w = [int(input()) for i in range(N)]

cs = [0]

for i in range(N):
    cs.append(cs[-1] + w[i])
    
print(0)