zi = list(map(int, input().split()))
sig = False
ch = []

for i in zi[1:]:
    ch.extend(int(sig) for _ in range(i))
    sig = not sig

for i in range(zi[0]):
    print("".join(map(str, ch[i*zi[0]:(i+1)*zi[0]])))