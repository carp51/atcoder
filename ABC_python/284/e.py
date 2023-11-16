import math
T = int(input())

for i in range(T):
    t = int(input())

    for j in range(2, int(t**(1/3))+1):
        if t % j != 0:
            continue

        tmp = t // j

        p, q = tmp, j
        if p % q == 0:
            print(q, t // j ** 2)
        else:
            print(int(math.sqrt(p)), q)
        break
