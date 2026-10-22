L = int(input())
s = 0
num = 1
count = 0
while True:
    num += 1
    flag = False
    for i in range(2, num):
        if num%i == 0:
            flag = True
            break
    if not flag:
        if s + num <= L:
            s += num
            count += 1
            print(num)
        else:
            break
print(count)