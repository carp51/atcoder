H, M = map(int, input().split())

count = 0

for h in range(H, 60):
    count += 1
    h = h % 24
    for m in range(0, 60):
        if count == 1:
            if m < M:
                continue
        
        h = str(h).zfill(2)
        m = str(m).zfill(2)

        tmp = h

        tmp_h = h[0] + m[0]
        tmp_m = tmp[1] + m[1]

        if 0 <= int(tmp_h) <= 23 and 0 <= int(tmp_m) <= 59:
            print(h, m)
            exit()