N = int(input())
score = [list(map(int, input().split())) for _ in range(N)]
total = [sum(i) for i in score]
ct = 0

for i in range(N):
    a = score[i]   
    for j in range(i+1, N):
        b = score[j]
        if (abs(total[i] - total[j]) <= 10 
                and abs(a[0] - b[0]) <= 5 
                and abs(a[1] - b[1]) <= 5 
                and abs(a[2] - b[2]) <= 5):
            ct += 1

print(ct)