cash = 0
saved = 0
month = 0

for i in range(1,13):
    cost = int(input())
    cash += 300

    if cash < cost:
        month = i
        break

    cash -= cost
    deposit = cash//100 * 100
    saved += deposit
    cash -= deposit

if month:
    print(-month)
else:
    print(cash + saved*6//5)