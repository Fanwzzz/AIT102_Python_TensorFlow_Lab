n = int(input())
cipher = input()
base = ord("a")

print("".join([chr((ord(ch) + n - base)%26 + base) for ch in cipher]))