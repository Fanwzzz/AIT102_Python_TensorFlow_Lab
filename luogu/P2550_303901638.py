n = int(input())
bonus = set(map(int, input().split()))
prize = [0] * 8

for _ in range(n):
    ticket = map(int, input().split())
    ct = sum(number in bonus for number in ticket)
    prize[ct] += 1

print(*prize[:0:-1])