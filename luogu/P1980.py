n, x = map(int, input().split())
x = str(x)
count = 0
for i in range(n):
    for j in str(i+1):
        if j == x:
            count += 1
print(count)