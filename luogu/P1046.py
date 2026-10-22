a = sorted(map(int, input().split()))
h = int(input())+30
for i in range(10):
    if h<a[i]:
        break
print(i)