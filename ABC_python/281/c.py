N, T = map(int, input().split())
A = list(map(int, input().split()))

total = 0
for a in A:
    total += a

now = T % total
if now == 0:
    now = total

now_song = 0
for i, a in enumerate(A):
    now_song += a
    if now <= now_song:
        song_number = i + 1
        song_time = a - (now_song - now)
        break

print(song_number, song_time)