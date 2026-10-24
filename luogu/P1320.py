ch = [input()]
zi = [len(ch[0]),]
ch.extend(input()for _ in range(zi[0]-1))

chj = "".join(ch)
ct = 0
sig = False

for i in chj:
    if int(i) == int(sig):
        ct += 1
    else:
        zi.append(ct)
        sig = not sig
        ct = 1

zi.append(ct)
print(*zi)