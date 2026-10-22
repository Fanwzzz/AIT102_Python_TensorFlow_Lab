s = float(input())
step = 0
swim = 0.0

while True:
    if swim >= s:
        break
    swim += 2*(0.98**step)
    step += 1
print(step)