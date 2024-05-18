H = int(input())
h = 0
cnt = 0

while h <= H:
    h += 2 ** cnt
    cnt += 1

print(cnt)
