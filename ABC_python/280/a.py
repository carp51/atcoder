def count_pieces(H, W, S):
    count = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                count += 1
    return count

H, W = map(int, input().split())
S = []
for _ in range(H):
    S.append(input())
print(count_pieces(H, W, S))