a, b = map(int, input().split())
ans = []

def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False

    for i in range(3, int(x**0.5) + 1, 2):
        if x % i == 0:
            return False
    return True

for half in range(1,10000):
    s = str(half)
    pal = int(s + s[:-1][::-1])
    if b >= pal >= a and is_prime(pal):
        ans.append(pal)

if a <= 11 <= b:
    ans.append(11)

for x in sorted(ans):
    print(x)