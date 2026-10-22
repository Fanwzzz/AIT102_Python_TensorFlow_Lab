num = sorted(map(int, input().split()))
ord = input().strip()
val = {"A":num[0], "B":num[1], "C":num[2]}
print(*(val[ch] for ch in ord))