L = int(input())
s = 0
num = 1
ct = 0

if L >= 2:
    s += 2
    ct +=1
    print(2)

while True:
    is_prime = True
    num += 2
    for i in range(3, num, 2):
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