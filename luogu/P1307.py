N = input()
if N[0] != "-":
    print(int(N[::-1]))
else:
    print("-", int(N[1:][::-1]), sep="")