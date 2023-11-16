X = int(input())

num = [50]

for i in range(1, 4):
    for j in range(1, 21):
        num.append(i * j)
        
N = len(num)
        
for i in range(N):
    for j in range(N):
        for k in range(N):
            if num[i] + num[j] + num[k] == X:
                print(True)
                exit(0)
                
            if num[i] + num[j] == X:
                print(True)
                exit(0)
                
            if num[i] == X:
                print(True)
                exit(0)
            
                
print(False)