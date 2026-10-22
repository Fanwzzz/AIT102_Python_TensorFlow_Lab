num = int(input())
a = num%2 == 0
b = num>4 and num<=12
print(int(a and b), int(a or b), int(a^b), int(not(a or b)))