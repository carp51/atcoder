A = []
while True:
    try:
        a = int(input())
        A.append(a)
    except:
        break
    
A.reverse()

for i in A:
    print(i)
    