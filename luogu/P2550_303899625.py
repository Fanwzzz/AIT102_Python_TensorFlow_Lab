n = int(input())
bonus = list(map(int, input().split()))
prize = [0,0,0,0,0,0,0,0]
for _ in range(n):
    ct = 0
    ticket = list(map(int, input().split()))
    for i in range(7):
        if bonus[i] in ticket:
            ct += 1
    prize[ct] += 1
print(*prize[:0:-1])