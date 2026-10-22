L = int(input())
s = 0
num = 1
ct = 0

while True:
    is_prime = True
    num += 1
    for i in range(2, num):
        if i > int(num**0.5)+1:
            break
        if num%i == 0:
            is_prime = False
            break
    if is_prime:
        if s+num > L:
            break
        else:
            s += num
            ct += 1
            print(num)
print(ct)