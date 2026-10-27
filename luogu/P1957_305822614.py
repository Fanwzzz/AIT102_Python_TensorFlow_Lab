i = int(input())

for _ in range(i):
    ls = list(input().split())

    if ls[0] == "a" or ls[0] == "b" or ls[0] == "c":
        sta = ls[0]
        a = int(ls[1])
        b = int(ls[2])
    else:
        a = int(ls[0])
        b = int(ls[1])
    
    match sta:
        case "a":
            tp = f"{a}+{b}={a+b}"
        case "b":
            tp = f"{a}-{b}={a-b}"
        case "c":
            tp = f"{a}*{b}={a*b}"
    print(tp)
    print(len(tp))