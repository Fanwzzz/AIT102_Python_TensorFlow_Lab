def isPrime(n):
    if n < 2:  
        return False
    if n == 2:
        return True
        
    for i in range(2, int(n ** (0.5))+1):
        if n%i ==0:
            return False
    return True

word = input()
freq = {}

for ch in word:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

maxn = max(freq.values())
minn = min(freq.values())
dif = maxn - minn

if isPrime(dif):
    print("Lucky Word")
    print(dif)
else:
    print("No Answer")
    print(0)