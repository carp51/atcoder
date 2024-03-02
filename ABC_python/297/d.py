a, b = map(int, input().split())
count = 0
while a != b:
    if a > b:
        if a % b == 0:
            count += a // b - b // b
            break
        tmp = a // b
        a -= tmp * b
        count += tmp
    else:
        if b % a == 0:
            count += b // a - a // a
            break
        tmp = b // a
        b -= tmp * a
        count += tmp

print(count)
