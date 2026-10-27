n = int(input())
cipher = list(input())

print("".join([chr((ord(i) + n - 97)%26 + 97) for i in cipher]))