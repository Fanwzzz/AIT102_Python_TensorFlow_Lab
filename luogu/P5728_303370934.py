N = int(input())
score = [list(map(int, input().split())) for _ in range(N)]
ct = 0

for i in range(N):
    for j in range(i+1, N):
        if abs(sum(score[i]) - sum(score[j])) <= 10 and abs(score[i][0] - score[j][0]) <= 5 and abs(score[i][1] - score[j][1]) <= 5 and abs(score[i][2] - score[j][2]) <= 5:
            ct += 1

print(ct)