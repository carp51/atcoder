S = [input() for _ in range(9)]

ans = 0

check = []

for i in range(9):
    for j in range(9):
        for x in range(i, 9):
            for y in range(j, 9):
                if i == x and j == y:
                    continue

                if S[i][j] == "." or S[x][y] == ".":
                    continue
                
                dx, dy = y - j, x - i

                if not (0 <= j - dy < 9 and 0 <= i + dx < 9):
                    continue

                if not (0 <= y - dy < 9 and 0 <= x + dx < 9):
                    continue

                if S[i + dx][j - dy] == "#" and S[x + dx][y - dy] == "#":
                    ans += 1

                    tmp = [[i, j], [x, y], [i + dx, j - dy], [x + dx, y - dy]]
                    tmp.sort()

                    check.append(tmp)

check.sort()
for i in range(1, len(check)):
    if check[i] == check[i - 1]:
        ans -= 1

print(ans)